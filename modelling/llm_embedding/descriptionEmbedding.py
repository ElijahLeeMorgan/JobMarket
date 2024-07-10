from torch import topk
from json import load
from warnings import filterwarnings
from sentence_transformers import SentenceTransformer
import pandas as pd

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

'''
def compareStudentDescription(compareDescription: list[str], printTopScores:bool=False, numOutputScores:int=5) -> list[float, int]:
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    filePath = "./data/jobDescriptionEmbeddings.csv"

    print("Loading degree embeddings...")
    compareDescription_embedding = loadEmbeddings(pathToFile="./data/degreeDescriptionEmbeddings.csv")
    #print("Encoding student description...")
    #compareDescription_embedding = model.encode(compareDescription, convert_to_tensor=True, show_progress_bar=True)
    print("Loading job embeddings...")
    description_embedding = loadEmbeddings(pathToFile=filePath)
    top_k = min(numOutputScores, len(description_embedding))

    # Compute cosine-similarities. I know this isn't good for context, but it works pretty well..
    similarity_scores = model.similarity(compareDescription_embedding, description_embedding)[0]
    scores, indicies = topk(similarity_scores, k=top_k)

    print(f"Top {numOutputScores} mo st similar sentences in database:")
    outputScores = zip(scores, indicies)
    
    if printTopScores:
        for score, index in outputScores:
            print(f"{index}: {readData()[index][:50]}... | Score: {score}")
    return outputScores
'''

def matchJobsHelper(data):
    result = []
    for embedding in data:
        split_floats = embedding.split(",")
        tensor = []
        for num in split_floats:
            tensor.append(float(num))
        result.append(tensor)
    return result


def matchJobsToDegree(jobDataFrame:pd.DataFrame, printOutput:bool=False, numOutputScores:int=5, degreeChoice:int=-1) -> pd.DataFrame:
    jobs = jobDataFrame
    degrees = pd.read_json("../../data_acquisition/finalized_data/bachelor_degree_information.json") # Hardcoded for now (forever).
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    numOutputs = max(len(jobDataFrame["embedding"]), numOutputScores)

    #TODO Rewrite as an error/warning.
    if degreeChoice < 0 or degreeChoice > 10:
        inStr = input("Choose a degree from the following:\n" + "\n".join(degrees) + "\n")
        if inStr.isnumeric():
            degreeChoice = (int(inStr) % 11) - 1
        else:
            print("Please enter a number.")

    print("Retrieving job embeddings...") if printOutput else None
    jobEmbeddings = jobs["embedding"]

    print("Loading degree embeddings...") if printOutput else None
    degreeEmbeddings = degrees["embedding"]

    # Please oh god do not look into this fucking mess, holy steezus christo.
    jobEmbeddings = matchJobsHelper(jobEmbeddings)
    degreeEmbeddings = matchJobsHelper(degreeEmbeddings)

    print(f"Top {numOutputScores} most similar sentences in database:") if printOutput else None

    simScores = model.similarity(degreeEmbeddings[degreeChoice], jobEmbeddings)[0]
    scores, indicies = topk(simScores, k=numOutputs)
    
    jobs.insert(len(jobs.columns), "similarityScore", scores)

    print(jobs) if printOutput else None
    return jobs
    



# Example usage.
if __name__ == "__main__":
    filterwarnings("ignore")
    testData = pd.read_json("../../data_acquisition/finalized_data/finalized_data.json")
    matchJobsToDegree(testData, printOutput=True, degreeChoice=5, numOutputScores=5)
    
