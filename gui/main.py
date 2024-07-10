import pandas as pd
from sentence_transformers import util
import torch
import ast


# Define weights for the ranking
weights = {
    'similarity_score': 0.96,
    'min_salary': 0.025,
    'max_salary': 0.015
}


# df = dataframe, ms = min_salary, wl = workload, ct = contract_type, sp = study_program
def controller(df, ms, wl, ct, sp):
    # Filter jobs based on user input
    filtered_df = filter(df, ms, wl, ct)
    if filtered_df.empty:
        return pd.DataFrame({'Message': ['No jobs found for the selected criteria.']})

    # Score the filtered jobs against the study program
    scored_df = score(filtered_df, sp)
    if scored_df.empty:
        return pd.DataFrame({'Message': ['No jobs found matching the study program criteria.']})

    # Rank the jobs with the weighted features
    ranked_df = ranking(scored_df)
    if ranked_df.empty:
        return pd.DataFrame({'Message': ['No jobs found after ranking. Criteria may be too restrictive.']})

    # Display the ranked jobs
    result_df = prep(ranked_df)
    return result_df


def filter(df, ms=0, wl=None, ct="any"):
    # Ensure columns are numeric
    df['max_salary'] = pd.to_numeric(df['max_salary'], errors='coerce')
    df['min_workload'] = pd.to_numeric(df['min_workload'], errors='coerce')
    df['max_workload'] = pd.to_numeric(df['max_workload'], errors='coerce')

    df = df[df['max_salary'] >= ms]
    df['diff_salary'] = df['max_salary'] - ms

    if wl is not None:
        df = df[df['max_workload'] >= wl]

    if ct != "any":
        df = df[df['contract_type'] == ct]

    return df


def convert_embeddings(embeddings):
    # Convert string embeddings back to tensors
    return [torch.tensor(ast.literal_eval(e)) if isinstance(e, str) else e for e in embeddings]


def score(df, sp):
    # Convert embeddings to tensors
    job_embeddings = convert_embeddings(df['embedding'].tolist())
    sp_embedding = convert_embeddings([sp['embedding'].iloc[0]])[0]

    # Compute cosine similarities using the Sentence-Transformers utility function
    cosine_scores = util.pytorch_cos_sim(sp_embedding, torch.stack(job_embeddings))

    # Extract the cosine scores as a flat list of scores and add to the dataframe
    df['similarity_score'] = cosine_scores[0].cpu().numpy()

    return df

def ranking(df):
    df['matching_score'] = ((weights['similarity_score'] * df['similarity_score']) +
                            (weights['min_salary'] * df['diff_salary']) +
                            (weights['max_salary'] * df['max_salary']))
    ranked_df = df.sort_values(by='matching_score', ascending=False)
    return ranked_df


def prep(result_df):
    # Create new columns for combined workload and salary
    result_df['combined_workload'] = result_df['min_workload'].astype(str) + ' - ' + result_df['max_workload'].astype(
        str) + '%'
    result_df['combined_salary'] = result_df['min_salary'].astype(str) + ' - ' + result_df['max_salary'].astype(
        str) + ' CHF'
    result_df['matching_score'] = (result_df['matching_score'].round(0)/100)
    return result_df