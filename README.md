<div align="center">
  <h1>Unequal Grounds: The Impact of Neighborhood Poverty on School Enrollment Across U.S. Regions</h1>
  <img src="project/Images/school.webp" width="500" height="300" alt="Project Logo">
</div>


<div align="center">

[![Python](https://img.shields.io/badge/python-3.11.9-blue.svg)](https://www.python.org/downloads/release/python-3119/)
[![Jayvee](https://img.shields.io/badge/jayvee-0.6.3-blue.svg)](https://pypi.org/project/jayvee/0.6.3/)
[![Jayvee](https://img.shields.io/badge/jayvee-0.6.4-blue.svg)](https://pypi.org/project/jayvee/0.6.4/)
[![Unit Test](https://img.shields.io/badge/Unit-Testing-blue.svg)](https://pypi.org/project/Unitesting)
[![Continuous Integration](https://img.shields.io/badge/Continuous-Integration-blue.svg)](https://pypi.org/project/Continuous-Integration)

[![Exercise Feedback](https://github.com/maazk9119/Data-Engineering-Pipeline/actions/workflows/exercise-feedback.yml/badge.svg)](https://github.com/maazk9119/Data-Engineering-Pipeline/actions/workflows/exercise-feedback.yml)
![Ex1](https://img.shields.io/badge/Ex1-100%25-brightgreen)![Ex2](https://img.shields.io/badge/Ex2-100%25-brightgreen)![Ex3](https://img.shields.io/badge/Ex3-100%25-brightgreen)![Ex4](https://img.shields.io/badge/Ex4-100%25-brightgreen)![Ex5](https://img.shields.io/badge/Ex5-100%25-brightgreen)
</div>

# Table of Contents

1. [Project Overview](#project-overview)
2. [Data Sources](#data-sources)
3. [Data Pipeline](#data-pipeline)
4. [Repository Structure](#repository-structure)
5. [License](#license)


## Project Overview
This project aims to explore the relationship between neighborhood poverty levels and school enrollment rates across North, Central, and South America, with a specific focus on the United States.

The main objectives are:
1. How neighborhood poverty correlates with school enrollment rates in U.S ?

2. Regional disparities in poverty  and their potential implications for educational equality ?

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

## Repository Structure
- `.github/workflows`: GitHub Actions workflows.
- `data/`: Raw and processed data files.
- `examples/`: Scripts and notebooks for running and trying out examples.
- `exercises/`: Jayvee exercises.
- `project/`: Main project folder.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `README.md`: Project overview and instructions.

## License
Both datasets I finalized have open licenses allowing public use and redistribution:

School Neighborhood Poverty Estimates (2020-21) dataset is licensed under the CC BY 4.0 license (Creative Commons Attribution 4.0 International License). This license allows public to share and adapt the data, provided that appropriate credit is given, and any derived works are shared under the same license. 

Common Core of Data (CCD) - School Nonfiscal Data Files and Documentation, 2018-19 dataset is also licensed under the CC BY 4.0 license. This similarly allows public use, distribution, and modification as long as proper attribution is given. 

Therefore, The content of this project is licensed under the Open Licenses and Creative Commons Attribution 4.0 International (CC BY 4.0) license. For more information, visit [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/) and [Open Licenses](https://resources.data.gov/open-licenses/)

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://licensebuttons.net/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
