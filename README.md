<div align="center">
  <h1>Unequal Grounds: The Impact of Neighborhood Poverty on School Enrollment Across U.S. Regions</h1>
  <img src="project/Images/school.webp" width="400" height="300" alt="Project Logo">
</div>


<div align="center">

[![Python](https://img.shields.io/badge/python-3.11.9-blue.svg)](https://www.python.org/downloads/release/python-3119/)
[![Jayvee](https://img.shields.io/badge/jayvee-0.6.3-blue.svg)](https://pypi.org/project/jayvee/0.6.3/)

[![Exercise Feedback](https://github.com/maazk9119/Data-Engineering-Pipeline/actions/workflows/exercise-feedback.yml/badge.svg)](https://github.com/maazk9119/Data-Engineering-Pipeline/actions/workflows/exercise-feedback.yml)
![Ex1](https://img.shields.io/badge/Ex1-100%25-brightgreen)![Ex2](https://img.shields.io/badge/Ex2-100%25-brightgreen)
</div>

# Table of Contents

1. [Project Overview](#project-overview)
2. [Data Sources](#data-sources)
3. [Data Pipeline](#data-pipeline)



## Project Overview
This project aims to explore the relationship between neighborhood poverty levels and school enrollment rates across North, Central, and South America, with a specific focus on the United States.

The main objectives are:
1. How does neighborhood poverty level impact school enrollment rates across different regions in the United States?

2. How do poverty levels around schools vary by region in the United States, and what might these differences suggest about educational inequality?

## Data Sources
The project utilizes the following datasets:
- **School Neighborhood Poverty Estimates (2020-21)**: Neighborhood poverty levels surrounding schools.
- **Report Card Enrollment (2022-2023)**: School enrollment statistics disaggregated by school, district, and state for the 2022-23 school year.

## Data Pipeline
The data pipeline consists of three main modules:
1. **Extractor**: Extracts data from URLs.
2. **Transform**: Performs necessary data transformations including deletion of useless columns and standardization of date formats.
3. **Loader**: Loads transformed data into an SQLite database.

The ETL process ensures data quality, consistency, and appropriate format alignment with research questions.

<div align="center">
  <img src="project/Images/ETL.webp" width="700" height="250" alt="ETL_Pipeline">
</div>
