# `JobMarket` - Project Charta
<!--- Content Based Job Filtration System-->

## Problem Definition
Students often lack clear insights into the job market, making it difficult for them to understand where they can apply their skills and what opportunities are available. Existing career resources are often outdated/not specific enough to provide insights, especially in Zürich. Our product provides students with a curated job selection that aligns closest to their skills and certifications.

<!---
This includes a summary of the most important findings from the user analysis: relevant segments and user groups. Describe the problems and needs of the users of the product to be developed. 
-->
## User Analysis

Students from ZHAW: 
- Students struggling finding jobs, our product finds jobs relevent to their field. 
- Students also struggle understanding the standard pay is for their job.

<!---
Schools:
- Adjusting the curiculum to changes in the job market.

Employers:
- Faster hiring to posting time and reduced hiring costs.

Stakeholders: List the people involved in and affected by the project. Describe their goals and relationships with each other. Visualisation in the form of a stakeholder map can provide a quick overview.
-->
## Stakeholders:
- JobCloud AG: Providing the Data for our product.
- Students: Customers of our product.

<!---
- Schools: Customers of our project.
- Employers: Hire new, quality, employees as fast as possible. In addition, they provide data to JobCloud AG.

You can reference more detailed analyses such as individual "personas" or interviews in separate documents in the appendix.
-->

## Situation Assessment
### Personnel
- Gian Würgler
- Melina Otth
- Dillon Moesch
- Elijah Morgan

### Material
- Laptops
- Internet
<!-- ^^^ We didn't really know what to put here. ^^^ -->

### Software
- Python 3.11+
- Visual Studio Code
- PyCharm
- BeautifulSoup
- Streamlit
- mydata-python
- word2vec
<!--- SQL, MySQL, etc? -->

<!---
Describe the available resources (personnel, material, (software) tools, infrastructure, etc.) and time as well as restrictions and constraints. Possible risks that may arise during the project are also identified.
-->

## Project Goals and Success Criteria
<!---
When is the project successful from a client/stakeholder perspective: Formulate (qualitative) objectives, wherever possible, corresponding key metrics and the target values to be achieved within the project.

It is also often helpful to specify what is explicitly excluded from the project objectives (out of scope).
-->
### Goals
<!--- TODO Subject to change, Python is slow. -->
- Find the best matches according to: similarity of the degree to the job, salary and filter for workload percentage, salary and contract type.
- Factors declaring the best match: Skill matching requierments in %, salary difference from the desired salary (descending) -- based on weights 0.96*score + 0.04*difference
- Runtime of 10 seconds or less.
- Application size under 50mb.
<!--- TODO Change this ^^^ -->
- Predict salaries within 20,000 CHF per year.

### Out of Scope
- Providing benefits/services to employers and schools.
- Dedicated database server.
- Consistent database updates.
- Distance or location preferences.
- User Interface.
- Regions other than Zurich.

### Data Mining Goals
- LLM prediction: Salary Prediction based on best working combination of available features about the job.
  - Measuerment: RMSE
  - overlap of salary range and predicted salary range in %.
- Matching: Vectorization/Embedding of job descriptions and program descriptions.
   - Measuerment: Similarity score. 

<!---
Map the problem definition, datasets to be used and primary objective onto a data mining task, e.g.:

* Classification
* Regression
* Clustering
* Outlier Detection
* Association rule learning (market basket analysis)
* Recommender System
* Visualisation
* ...

Along with the definition of the actual technical problem (category) to be solved, 
the project goals must be mapped onto quitable quantitative metrics and corresponding target values. For example, for a classification task one might specify an *F-score* of 0.9 as a minimal requirement for an acceptable solution.  
Such a requirement should be aligned with the overall project goals and/or literature references or justified by other references, respectively.
-->

## Project Plan

<!---
Divide the project into individual phases, describe them briefly and draw up a preliminary timetable, e.g. as a Gantt chart:
Ranking Matching: Type of Job? -> Skills -> Prefrences -> Salary -->

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    tickInterval 5day
    section Project Charta
        Define problem goals :a1, 2024-07-01, 2d
    section Plan
        Complete Project charta :a2, 2024-07-01, 2d
        Create project plan :a3, 2024-07-01, 2d
    section Data Acquisition and Exploration
        Scraping :a4, 2024-07-02, 2d
        Data Report :a5, 2024-07-03, 2d
    section LLM prediction Problem
        Model Development :a6, 2024-07-04, 4d
        Model Report :a7, 2024-07-08, 1d
        Evaluation Log :a8, 2024-07-08, 1d
    section Matching Problem
        Model Development :a9, 2024-07-05, 4d
        Model Report :a10, 2024-07-09, 1d
        Evaluation Log :a11, 2024-07-09, 1d
    section Streamlit visualisation
        Create Streamlit webpage :a12, 2024-07-09, 2d
    section Presentation
        Prepare Presentation :a13, 2024-07-10, 1d
    section Revision
        Revision :a14, 2024-07-11, 1d
    section Milestones
        Project checkpoint: milestone, m1, 2024-07-04, 4m
        Project presentation: milestone, m2, 2024-07-11, 15m

```
See [Mermaid syntax for Gantt charts](https://mermaid.js.org/syntax/gantt.html).

## Roles and Contact Details
List the people involved in the development work here with their role titles, tasks and contact details
Melina Otth, Team Lead, otthmel1@students.zhaw.ch
Elijah Morgan, Developer, morgaeli@mail.gvsu.edu
Dillon Moesch, Developer, moeschd@mail.gvsu.edu
Gian Wurgler, Developer, wuerggia@students.zhaw.ch
<!--- TODO add titles.-->
