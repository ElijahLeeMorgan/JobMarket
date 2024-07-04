from torch import topk
from json import load
from warnings import filterwarnings
from sentence_transformers import SentenceTransformer

# This file is used to generate embeddings for job descriptions and compare them to a student's description.

''' I was about to classify everything, but I'd have to write "self." everywhere, and it's not worth my time.
class DescriptionEmbedding:
    def __init__(self) -> None:
        self._model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        self._filePath = "../data/jobDescriptionEmbeddings.csv"
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def filePath(self):
        return self._filePath
    
    @filePath.setter
    def filePath(self, filePath):
        self._filePath = filePath
'''    

# Reads data from JSON file.
def readData() -> list[str]:
    with open("../../data_acquisition/data/all_jobs_data.json", "r", encoding="utf-8") as file:
        allData = load(file)
        data = []
        for i in range(len(allData[:])): # Sorta hacky, but it works
            data.append(allData[i]["description"])
        file.close()
    return data

# Embedding Storage Helpers
def storeEmbeddings(tensors: list[list[float]], pathToFile: str = "./embeddings.csv") -> None:
    with open(pathToFile, "a", encoding="utf-8") as file:
        for tensor in tensors:
            file.write(",".join([str(x) for x in tensor.tolist()]) + "\n")
        file.close()

def clearEmbeddings(pathToFile: str = "./embeddings.csv") -> None:
    with open(pathToFile, "w", encoding="utf-8") as file:
        file.write("")
        file.close()

def loadEmbeddings(pathToFile: str = "./embeddings.csv") -> list[list[float]]:
    with open(pathToFile, "r", encoding="utf-8") as file:
        embeddings = []
        for line in file:
            embeddings.append([float(x) for x in line.split(",")])
        file.close()
    return embeddings

# Generate Embeddings, takes about 2 minutes to run. Only needs to be run once per DB update.
def generateEmbeddings(compareDescription: list[str]) -> None: # WARNING: This fucntion will delete the original contents of the file!
    filePath = "./data/jobDescriptionEmbeddings.csv"
    descriptions = readData()
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

    print("Encoding job descriptions...")
    description_embedding = model.encode(descriptions, convert_to_tensor=True, show_progress_bar=True)
    print("Clearing embeddings...")
    clearEmbeddings(pathToFile=filePath)
    print("Storing embeddings...")
    storeEmbeddings(description_embedding, pathToFile=filePath)


def compareStudentDescription(compareDescription: list[str], printTopScores:bool=False, numOutputScores:int=5) -> list[float, int]:
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    filePath = "./data/jobDescriptionEmbeddings.csv"

    print("Encoding student description...")
    compareDescription_embedding = model.encode(compareDescription, convert_to_tensor=True, show_progress_bar=True)
    print("Loading embeddings...")
    description_embedding = loadEmbeddings(pathToFile=filePath)
    top_k = min(numOutputScores, len(description_embedding))

    # Compute cosine-similarities. I know this isn't good for context, but it works pretty well..
    similarity_scores = model.similarity(compareDescription_embedding, description_embedding)[0]
    scores, indicies = topk(similarity_scores, k=top_k)

    print(f"Top {numOutputScores} most similar sentences in database:")
    outputScores = zip(scores, indicies)
    
    if printTopScores:
        for score, index in outputScores:
            print(f"{index}: {readData()[index][:50]}... | Score: {score}")
    return outputScores

''' Example Usage:
if __name__ == "__main__":
    filterwarnings("ignore")
    compareStudentDescription(["Batchelor's Degree, 80% workload, and Java are my best skills."], printTopScores=True)
'''
