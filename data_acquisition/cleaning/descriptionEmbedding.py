from torch import topk
from json import load
from warnings import filterwarnings
from sentence_transformers import SentenceTransformer

def readData(rows=100) -> list[str]:
    with open("../data/all_jobs_data.json", "r", encoding="utf-8") as file:
        allData = load(file)
        data = []
        for i in range(len(allData[:])): # Sorta hacky, but it works
            data.append(allData[i]["description"])
    return data

def embedDescription(compareDescription: list[str], printTopScores:bool=False, numOutputScores:int=5) -> list[float, int]:
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    descriptions = readData()
    top_k = min(numOutputScores, len(descriptions))
    
    #TODO Store encodings for faster runtime, update only when DB updates.

    print("Encoding student description...")
    compareDescription_embedding = model.encode(compareDescription, convert_to_tensor=True, show_progress_bar=True)
    print("Encoding job descriptions...")
    description_embedding = model.encode(descriptions, convert_to_tensor=True, show_progress_bar=True)

    # Compute cosine-similarities. I know this isn't good for context, but it's a start.
    similarity_scores = model.similarity(compareDescription_embedding, description_embedding)[0]
    scores, indicies = topk(similarity_scores, k=top_k)

    #print("\nDescription:", description)
    print(f"Top {numOutputScores} most similar sentences in corpus:")
    outputScores = zip(scores, indicies)
    
    if printTopScores:
        for score, index in outputScores:
            print(f"{descriptions[index]}, Score: {score}")
            
    return outputScores

if __name__ == "__main__":
    filterwarnings("ignore")
    embedDescription(["The powerhouse of the cell is the mitochondria."], printTopScores=True)