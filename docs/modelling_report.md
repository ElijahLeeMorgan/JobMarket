# `Job Market Analysis` - Modelling Report
## Initial situation
- Data Source: The dataset was derived from Jobs.ch and included comprehensive job listing details such as company names, job titles, descriptions, and workload, focusing on tech jobs in the Zurich/Schaffhausen region.
### Salary prediction LLM:
- Objective: Our project aimed to leverage advanced machine learning models to predict missing salary data and enhance job matching capabilities.
- Technological Backbone: We chose the LLaMA3-70B model developed by Meta due to its large context window of 8,192 tokens, which supports complex input and output relationships.

### Embedding & Cosinus Similarity
- Objective: Our project aimed to rank similarity of job descriptions to degree descriptions while improving job matching accuracy via Machine Learning technologies.
- Technological Backbone: We choose the paraphrase-multilingual-MiniLM-L12-v2 model developed by the Association for Computational Linguistics due to it's cross-lingual capabilites while maintaing a high degree of accuracy.

- Matching program and job descriptions via cosinus similarity.
- Jobs.ch provided all our data on Tech jobs in the Zurich/Schaffhausen reigon.
- Independant varibles: Company, Salary (if applicable), Workload, Job Description, Degree Description, Degree Requirements. 
- Dependant varibles: Predicted Salaries (if applicable), Similarity Score, Job Ranking


## Model Descriptions
### Salary prediction LLM:
#### LLaMA3-70B Model Configuration:
- Model ID: llama3-70b-8192
- Developer: Meta
- Purpose: Selected for its capability to process extensive data blocks and generate accurate predictions based on job listing details.
#### Prompt Engineering:
- Utilized direct features from the dataset: Job title, company, min workload, max workload, contract type and job descriptions. Start with one feature and with each try add one more.
- Few-Shot Learning Approach: Began with a base block of five salary examples, incrementally adding data blocks, the same as the directed features, to assess improvements in predictive accuracy.
  - Block 0: Few shot 5 examples with salary 
  - Block 1: Job title 
  - Block 2: company 
  - Block 3: workload (min workload and max workload) 
  - Block 4: Contract type 
  - Block 5: description
### Embedding & Cosinussimilarity
- Model ID: [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)
- Developer: Huggingface
- Purpose: Selected for it's cross-lingual capabilities to accurately compare similarity of job and degree descriptions.
- Library: [SentenceTransformers 3.0.1](https://www.sbert.net/)

<!---
## Results
Key figures dependent on the model and modelling objective

- RMSD, ROC/Lift-Charts, AUC, Confusion Matrix, Accuracy, Precision, Recall
- Coherence, Perplexity, ... 
- If applicable: analyses/plots of (hyper)parameter screenings
-->

## Model Interpretation
### Salary prediction LLM:
#### Evaluation:
- Labled Dataset: 106 data points with salaries for evaluation and 5 for few-shot learning setup.
- Unlabled Dataset: Comprised of job listings lacking salary information.
- Metrics Used: RMSE and Overlap Coefficient, with a focus on how each block addition impacted performance.
- Best Results: Block 1, focusing on the job title, yielded an RMSE of 19,828.07 and an Overlap Coefficient of 0.43.
#### Challenges:
- Faced API rate limits which paused the modeling process, reflecting the need for strategic session management and possibly seeking more robust API access for future tasks.

### Embedding & Cosinussimilarity
#### Evaluation:
- Functionality: Successfully aligned job opportunities with candidate skills and preferences.
- Region Focus: Restricted to tech jobs within the Zurich/Schaffhausen region, effectively narrowing down potential job matches for local students.
#### Challenges
- Data Type Mismatches: Encountered issues with datatype conversions in job descriptions, suggesting the need for enhanced data handling or content generation.
- Data Integration: Challenges in maintaining data structure integrity while merging generated embeddings with the main dataset.
## Conclusions and next steps
### Salary prediction LLM:
#### Achievements: 
- Successfully integrated an LLM to predict salaries and match job descriptions effectively, demonstrating the feasibility and efficiency of using AI in real-world job market scenarios.
#### Limitations and Improvements:
- Currently limited to tech jobs in the Zurich region. Expanding to other industries and regions could enhance the model’s utility and applicability.
- Our analysis is presently confined to job listings exclusively sourced from Jobs.ch. To enhance the diversity and representativeness of our dataset, one could expande the scope of our data collection to include multiple job portals.
- Transition to fine-tuned models for specific data subsets to improve accuracy and relevance.
#### Future Directions:
- Include a broader range of job listings from multiple sources to diversify the data and enhance model robustness.
- Implement a permanent database solution for ongoing data management and model training.
#### Deployment: 
- The model's predictions can be utilized in real-time if integrated within a dynamic job-matching platform, ensuring continuous relevance and utility.

### Embedding & Cosinussimilarity
#### Achievements:
- Effective in reducing job search time by accurately matching student profiles with available tech job openings.
#### Next Steps:
- Extend the application of embedding and cosine similarity techniques to encompass a broader range of industries and job types, increasing the utility of our models across different sectors.