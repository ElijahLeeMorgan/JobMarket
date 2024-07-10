# `Sample Project` - Data Report
All information on the data used in the project is compiled in the data report in order to ensure the traceability and reproducibility of the results and to enable a systematic expansion of the database.

Typically, in the exploratory analysis of the acquired raw data, quality and other issues are identified, which require pre-processing, merging of individual datasets and feature engineering into processed datasets. Therefore, this template provides a separate section for the processed data, which then serves as a starting point for the modelling activities. This needs to be adapted to the specific project requirements.

## Raw data
### Overview Raw Datasets
| Name      | Quelle                                                                                 | Storage location |
|-----------|----------------------------------------------------------------------------------------|------------------|
| Dataset 1 | [Jobs.ch, Tech jobs in the Zurich Reigon](https://www.jobs.ch/de/stellenangebote/informatik-telekommunikation/?location=z%C3%BCrich&term=) | JobMarket\data_acquisition\data\all_jobs_data.json                 |
| Dataset 2 | (descriptions)                                                                         |                  |

### Data Acquisition
- Code Sharing: The scraping and data processing code is shared among team members via GitHub, ensuring transparency and collaborative development.

### Details Dataset 1
#### Dataset Overview
- Title: Job Listings from Zurich/Schaffhausen Region in Engineering Sector
- Collectors: Malina Otth, Elijah Morgan, Dillon Moesch, Gian Wurgler
- Purpose: This dataset was collected as part of the 2024 Summer School project focused on Job Market Analysis. The aim is to analyze job roles, demand in skills, and develop models for salary prediction and job recommendation systems. 
#### Data Collection
- Source: Jobs.ch
- Methodology: The data was scraped using BeautifulSoup, targeting job listings in the engineering sector within the Zurich and Schaffhausen regions.
- Criteria: Listings were selected based on location and industry. Only job listings that fit these criteria were included in the dataset.
#### Data Content
- Fields: Job title, company, contract type, salary, job description, workload.
- Salary Information:
  - Range: CHF 28,300 to CHF 262,080
  Available in 110 listings out of 1706
- Contract Types: Festanstellung (Permanent), Praktikum (Internship), Freelancer
- Workload: Represented as a percentage, indicating the minimum and maximum expected workload.
#### Data Description
- Data Details: Descriptions vary widely, providing insights into company culture, job roles, and specific qualifications required.
#### Data Integrity and Cleaning
- Missing Data: Salaries missing in some listings are planned to be predicted using a language model.
- Duplicates: No duplicates were found in the dataset, ensuring the uniqueness of each listing.
#### Data Security and Privacy
- Storage: The dataset is stored in CSV format on each team member's computer.
# da no ane schriebe wo date gspeicheret sind
#### Applications and Limitations
- Potential Uses: The dataset supports the development of a salary prediction model, job recommendation system, and analysis of in-demand skills within the specified region and sector.
- Limitations: Salary data is not available for all listings, which may affect the accuracy of the salary prediction model.

<!---
- Description of what information the dataset contains
- Details of the data source/provider
- Information on data procurement: description and possibly references to resources (download scripts, tools, online services, ...). Any new team member should be able to acquire the data indepentendently following these instructions.
- Legal aspects of data use, licences, etc.
- Data governance aspects: Categorisation of the data based on internal business requirements, e.g. public, business-relevant, personal
- If applicable: categorisation into dependent (target variable, regressor) and independent (regressor) variables
- ...
-->

#### Data Catalogue
The data catalogue basically represents an extended schema of a relational database.

| Column index | Column name   | Datatype | Values (Range, validation rules)                              | Short description                                         |
|--------------|---------------|-------|---------------------------------------------------------------|-----------------------------------------------------------|
| 0            | Index         | Integer |                                                               | Primary Key, Unique identifier for each job listing entry |
| 1            | title         | string|                                                               | Job title of the listing                                  |
| 2            | company       | string |                                                               | Name of the company offering the job                                                        |
| 3            | contract_type | string | Festanstellung (Permanent), Praktikum (Internship), Freelance | Type of employment contract offered                                                          |
| 4            | workload      | string | 0% - 100%                                                     | Expected workload expressed as a percentage range                                                         |
| 5            | salary        | Integer | from 28'300 to 140'000                                        | Annual salary or hourly wage offered for the position, expressed in CHF                                                          |
| 6            | description   | string |                                                               | Detailed description of the job including responsibilities, qualifications, and other relevant information                                                         |



### Data Quality Dataset 1
#### Data Collection Overview
- Collection Period: Data was scraped on July 2, 2024, ensuring that the information reflects the current job market conditions in the Zurich/Schaffhausen regions within the engineering sector.
#### Data Completeness
- Missing Data: The only column with missing data is the 'salary' column. Missing salary data are noted as "Salary not specified." This missing data was intentionally left as is, due to its unavailability at the source.
#### Data Accuracy
- Verification Process: A random sampling method was employed to verify the accuracy of job titles, company names, and salary details against information available on Jobs.ch and corresponding company websites.
- Results: The sampled entries corroborated the dataset’s accuracy, confirming that the job listings accurately represent the information as advertised on the original platforms.
#### Data Consistency
- Handling Inconsistencies: Salary data was presented in two formats: annual salary and hourly wage. Hourly wages were normalized to annual figures based on a 42-hour workweek multiplied by 52 weeks, ensuring consistency across the dataset for analytical purposes.
#### Data Uniqueness
- Duplicate Analysis: While no identical duplicates were found, the dataset contains multiple entries from the same companies, reflecting different job listings. This repetition is appropriate given the dataset's purpose to provide a comprehensive view of available opportunities in the specified sectors and regions.
#### Data Timeliness
- Relevance: The dataset is highly recent, scraped last week, making it extremely relevant for immediate analysis and use in predicting current market trends and demands.
#### Data Usability
- Accessibility and Extension: The dataset, along with the scraping code available on GitHub, allows for continuous updates and easy access, making it highly usable for ongoing job market analysis. Anyone with access to the scraping code can retrieve updated and current data, enhancing the dataset's utility over time.


## Processed Data
### Overview Processed Datasets
| Name | Quelle                                    | Storage location                                                                                                                                                              |
|----------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Processed Dataset 1      | [Jobs.ch, Tech jobs in the Zurich Reigon]([https://www.jobs.ch/en/vacancies/?region=7&term=](https://www.jobs.ch/de/stellenangebote/informatik-telekommunikation/?location=z%C3%BCrich&term=)                              | JobMarket\data_acquisition\data\df_with_salary.csv<br/> JobMarket\data_acquisition\data\df_without_salary.csv<br/> JobMarket\data_acquisition\data\df_with_salary_fewshot.csv |
| Processed Dataset 2      | Name/short description of the data source | Link and/or short description of the location where the data is stored, e.g. accessible to the team                                                                           |

### Details Processed Dataset 1
#### Workload Splitting:
The original 'workload' column, which ranged from 0% to 100%, has been divided into two separate columns: 'min_workload' and 'max_workload'. This split provides clearer insights into the range of expected work commitments for each position.
#### Salary Splitting:
The original 'salary' column has been divided into two separate columns: 'min_salary' and 'max_salary'. This split provides clearer insights into the range of expected salary for each position.
#### Contract Type Corrections:
Four instances of contract types were incorrectly scraped. These entries have been manually corrected to reflect the appropriate contract types, ensuring the accuracy of the employment classification in the dataset.
#### Salary Normalization:
Hourly wages have been converted to annual salaries based on a calculation of 42 hours per week over 52 weeks. This adjustment allows for a consistent salary comparison across all job listings.
Data Segmentation:
#### Usage Preparation
The dataset has been segmented into three distinct dataframes for specialized analysis:
- DataFrame for Few-Shot Prediction: Specifically prepared for training a machine learning model using few-shot learning techniques to predict missing salary data. 5 Data Points were taken.
- DataFrame with Salary: Contains all listings where salary information is provided except of the Data in the Few-Shot DataFrame.
- DataFrame without Salary: Comprises listings that do not specify salary details.

#### Data Catalogue

| Column Index | Column Name    | Datatype | Values (Range, Validation Rules)                               | Short Description                        |
|--------------|----------------|-------|----------------------------------------------------------------|------------------------------------------|
| 0            | Index          | Integer |                                                                | Primary Key                              |
| 1            | Title          | String|                                                                | Job title                                |
| 2            | Company        | String |                                                                | Company offering the job                 |
| 3            | Contract_Type  | String | Festanstellung, Praktikum, Freelancer                          | Type of employment contract offered      |
| 4            | Min_Workload   | String | 0% - 100%                                                      | Minimum expected workload as a percentage |
| 5            | Max_Workload   | String | 0% - 100%                                                      | Maximum expected workload as a percentage |
| 6            | Min_Salary     | Integer | From 28'300 to 100'000  | Minimum annual salary in CHF             |
| 7            | Max_Salary     | Integer | From 28'300 to 140'000  | Maximum annual salary in CHF             |
| 8            | Description    | String |                                                                | Detailed job description                 |



### Details Processed Dataset 2
- Description of what information the dataset contains
- Details and reasons for the processing steps -> Traceability and ensuring reproducibility
- How can the data be accessed? Description, scripts, tools, ...
- ...
