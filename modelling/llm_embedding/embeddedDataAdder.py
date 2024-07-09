import json

with open("modelling/llm_embedding/data/bachelor_degree_information.json", "r", encoding="utf-8") as jsonFile:
     data = json.load(jsonFile)


with open("modelling/llm_embedding/data/degreeDescriptionEmbeddings.csv", "r", encoding="utf-8") as embedding_info:
    embedding_info = embedding_info.readlines()
    job_index = 0
    for d in data:
        d["embedding"] = embedding_info[job_index]
        job_index += 1


with open("modelling/llm_embedding/data/bachelor_degree_information.json", "w", encoding="utf-8") as jsonFile:
    json.dump(data, jsonFile, ensure_ascii=False, indent=4)