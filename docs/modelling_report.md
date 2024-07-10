# `Job Market Analysis` - Modelling Report
## Initial situation
- Salary prediction based on workload percentage and company via an LLM.
- Matching program and job descriptions via a LLM.
- Jobs.ch provided all our data on Tech jobs in the Zurich reigon.
- Independant varibles: Company, Salary (if applicable), Workload, Job Description, Degree Description, Degree Requirements. 
- Dependant varibles: Predicted Salaries (if applicable), Similarity Score, Job Ranking

## Model Descriptions
- Salary prediction LLM:
- Description similarity LLM: [SentenceTransformers 3.0.1](https://www.sbert.net/) library with the: [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) pre-trained model.
<!--
- Graphical representation of the modelling pipeline

## Results
Key figures dependent on the model and modelling objective

- RMSD, ROC/Lift-Charts, AUC, Confusion Matrix, Accuracy, Precision, Recall
- Coherence, Perplexity, ... 
- If applicable: analyses/plots of (hyper)parameter screenings
-->

## Model Interpretation
- Sucessfully predicted Salary and matched student degrees to avaible jobs. 
- Based on our model findings, we can effectively match tech jobs to student skills and prefrences.
- Despite restrictions to tech industry jobs within the Zurich reigon, we're capable of reducing a student's job search.

## Conclusions and next steps
- Currenlty, our project is limited to tech jobs posted by Jobs.ch within the Zurich reigon.
- If this project were to continue through production, we'd expand the project to all industries in Zurich and pull from multiple data sources.
- In addition, our generic LLM models would be improved or replaced with fine-tuned LLM models. Finally, a true database solution would implemented to store and organize our data.