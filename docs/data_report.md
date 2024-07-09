# `Sample Project` - Data Report
All information on the data used in the project is compiled in the data report in order to ensure the traceability and reproducibility of the results and to enable a systematic expansion of the database.

Typically, in the exploratory analysis of the acquired raw data, quality and other issues are identified, which require pre-processing, merging of individual datasets and feature engineering into processed datasets. Therefore, this template provides a separate section for the processed data, which then serves as a starting point for the modelling activities. This needs to be adapted to the specific project requirements.

## Raw data
### Overview Raw Datasets
| Name      | Quelle                                                                                 | Storage location |
|-----------|----------------------------------------------------------------------------------------|------------------|
| Dataset 1 | [Jobs.ch, Jobs in the Zurich Reigon](https://www.jobs.ch/en/vacancies/?region=7&term=) | CSV              |
| Dataset 2 | (descriptions)                                                                         |                  |

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
Data Security and Privacy
Storage: The dataset is stored in CSV format on each team member's computer.
- Code Sharing: The scraping and data processing code is shared among team members via GitHub, ensuring transparency and collaborative development.
Applications and Limitations
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

| Column index | Column name   |  Datatype | Values (Range, validation rules) | Short description |
|--------------|---------------|---|---|---|
| 1            | title         |   |   |   |
| 2            | company       |   |   |   |
| 3            | contract_type |   |   |   |
| 4            | workload      |   |   |   |
| 5            | salary        |   |   |   |
| 6            | description   |   |   |   |


#### If applicable: Entity Relationship Diagram


#### Data Quality


## Processed Data
### Overview Processed Datasets
| Name | Quelle | Storage location |
|----------------|-----------------------------------------|--------------------------------------------------------------------------|
| Processed Dataset 1      | Name/short description of the data source | Link and/or short description of the location where the data is stored, e.g. accessible to the team |
| Processed Dataset 2      | …                                       | …                                                                        |

### Details Processed Dataset 1
- Description of what information the dataset contains
- Details and reasons for the processing steps -> Traceability and ensuring reproducibility
- How can the data be accessed? Description, scripts, tools, ...
- ...

#### Data Catalogue


#### If applicable: Entity Relationship Diagram


### Details Processed Dataset 2
...
