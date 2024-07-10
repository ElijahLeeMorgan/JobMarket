# `Job Market Analysis` - Decision Log

* Do results meet user needs? **Yes**
* Continuation of the project? **Yes**
* Planning of the deployment: **Incomplete**
* Carry out an additional data mining iteration: **Yes, several.**
    * Acquire more data from other job posting sites and ZHAW personnel or materials.
    * Fine-tuning and specialization of our modelling.
    * Build a scalable database solution.
    * Refactor our application for maintainability.


| Date       | Decision Item                            | Decision Made                                           | Reasoning Behind Decision                                      | Expected Impact                                      | Status      |
|------------|------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------|-------------|
| 2024-07-01 | Source of Data                           | To exclusively use data from Jobs.ch                    | Initial ease of access and familiarity with the platform       | Limit to variety and scope of job listings           | Done        |
| 2024-07-01 | Source of Study Program Data             | Use Data from zhaw.ch                                   | Specialize on study programs provided by the ZHAW              | Get good mapping for ZHAW students                   | Done        |
| 2024-07-02 | Choice of Machine Learning Model         | To use LLaMA3-70B-8192 for salary prediction            | Model's large context window suitable for complex job data     | Predict Salary                                       | Implemented |
| 2024-07-03 | Approach to Handling Missing Salary Data | Employ few-shot learning with incremental data blocks   | To refine model predictions through iterative testing          | Enhanced model precision and performance             | Completed   |
| 2024-07-05 | Handling of API Rate Limits              | Paused data collection and modeling during limit resets | To comply with API usage terms and avoid service interruptions | Delay in project timeline but ensured data integrity | Completed   |
| 2024-07-03 | Data Preprocessing Method                | Normalize hourly wages to annual salaries               | Consistency in salary data for comparative analysis            | Standardized data for more accurate analysis         | Completed   |
| 2024-07-03 | Description Embedding and Comparison     | Preprocessed embeddings for job and degree descriptions | To imporve model preformence and reduce app runtime            | Ability to rank jobs based on there relavence to each degree       | Completed |
| 2024-07-08 | Best Feature Selection for Model         | Use Few-Shot Block1                                     | Best Prediction based on RMSE and Overlab                      | Direct impact on model’s predictive accuracy         | Implemented |

