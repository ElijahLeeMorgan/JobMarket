import json

with open("data_acquisition/finalized_data/finalized_data.json", "r", encoding="utf-8") as jsonFile:
     data = json.load(jsonFile)


with open("modelling/llm_embedding/data/jobDescriptionEmbeddings.csv", "r", encoding="utf-8") as embedding_info:
    embedding_info = embedding_info.readlines()
    job_index = 0
    for d in data:
        d["embedding"] = embedding_info[job_index]
        job_index += 1


with open("data_acquisition/finalized_data/finalized_data.json", "w", encoding="utf-8") as jsonFile:
    json.dump(data, jsonFile, ensure_ascii=False, indent=4)