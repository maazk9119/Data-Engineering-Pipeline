# Project Plan

## Title

"Unequal Grounds: The Impact of Neighborhood Poverty on School Enrollment Across U.S. Regions"

## Main Questions

1. How does neighborhood poverty level impact school enrollment rates across different regions in the United States?

2. How do poverty levels around schools vary by region in the United States, and what might these differences suggest
   about educational inequality?

## Description


This project aims to explore the relationship between neighborhood poverty levels and school enrollment rates across North, Central, 
and South America, with a specific focus on the United States. By analyzing the School Neighborhood Poverty Estimates (2020-21) dataset[^r1] 
alongside the Common Core of Data (CCD)[^r2], this study seeks to uncover how varying poverty levels around schools influence educational access.
The research will investigate whether schools located in impoverished neighborhoods face challenges that result in lower enrollment rates, 
thereby shedding light on potential disparities in educational opportunities across different regions.

Ultimately, this research aspires to inform policymakers and educators about the pressing need for targeted interventions that address the 
impact of socioeconomic conditions on education. By highlighting the intersection of poverty and educational access, this project seeks to 
contribute to ongoing discussions about equity in education and the importance of fostering inclusive learning environments that support 
all students, regardless of their socioeconomic background​.

## Datasources


### Datasource 1:
* Metadata URL: https://catalog.data.gov/dataset/school-neighborhood-poverty-estimates-2020-21
* Data URL: https://catalog.data.gov/dataset/school-neighborhood-poverty-estimates-2020-21/resource/de9ce4ec-5171-40e7-9df2-72620efdd19a
* Data Type: CSV

This dataset from the National Center for Education Statistics (NCES) includes data on neighborhood poverty levels surrounding schools, which can serve as a proxy for educational access and community socioeconomic conditions.

### Datasource 2:
* Metadata URL: https://catalog.data.gov/dataset/report-card-enrollment-2022-23-school-year-year-end-update
* Data URL: https://catalog.data.gov/dataset/report-card-enrollment-2022-23-school-year-year-end-update/resource/97c9a15c-8e65-4795-87be-206527b89a86
* Data Type: CSV
  
This dataset provides detailed school enrollment statistics disaggregated by school, district, and state for the 2022-23 school year. It includes student counts by demographics, which can help analyze how regional poverty levels might influence enrollment and highlight disparities across regions.

## Work Packages
This project is structured into six work packages, represented as [milestones in the GitHub repository](https://github.com/maazk9119/Data-Engineering-Pipeline/milestones).
Each work package will contain at least one issue.

1. **Project Definition and Data Source Selection** [[WP1](https://github.com/maazk9119/Data-Engineering-Pipeline/milestone/1)]
    1. Define the research topic on a given theme.
    2. Define the research question on a selected topic.
    3. Locate potential data sources.
    4. Evaluate the identified data sources.
2. **Data Acquisition and Pipeline** [[WP2](https://github.com/maazk9119/Data-Engineering-Pipeline/milestone/2)]
    1. Determine the best data storage format.
    3. Data Pipeline.
3. **Data Exploration, Analytics and Report** [[WP3](https://github.com/maazk9119/Data-Engineering-Pipeline/milestone/3)]
    1. Conduct exploratory data analysis and preliminary visualization.
    2. Create DataLoader, Pipeline, Visualizations, Models, etc.
    3. Address all the research questions.
    4. Draw conclusions form the analysis. 
4. **Automated Testing** [[WP4](https://github.com/maazk9119/Data-Engineering-Pipeline/milestone/4)]
    1. Create Tests.
5. **Continuous integration** [[WP5](https://github.com/maazk9119/Data-Engineering-Pipeline/milestone/5)]
    1. Develop CI.
    2. Develop CI for Pre-Commit.
6. **Final Report** [[WP6](https://github.com/maazk9119/Data-Engineering-Pipeline/milestone/6)]
    1. Develop visual representations. 
    2. Enhance the repository's presentation. 
    3. Prepare the final presentation.
  
**Note:** Work packages must be completed sequentially as each one depends on the completion of all preceding ones.




## References and footnotes
[^r1]: https://catalog.data.gov/dataset/school-neighborhood-poverty-estimates-2020-21
[^r2]: https://catalog.data.gov/dataset/report-card-enrollment-2022-23-school-year-year-end-update
