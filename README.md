# Employee Attrition Analysis

## Project Overview

This project analyzes employee attrition using the IBM HR Analytics Employee Attrition & Performance dataset. The goal is to identify factors associated with employee attrition and develop a machine learning classification model to predict employees who may be at risk of leaving.

The project includes data cleaning, exploratory data analysis, statistical analysis, machine learning, and a custom Excel Dashboard.

## Research Question

What factors contribute to employee attrition, and how effectively can machine learning be used to identify employees who may be at risk of leaving?

## Dataset

The project uses the IBM HR Analytics Employee Attrition & Performance dataset. The dataset contains 1,470 employee records and includes information related to compensation, job level, overtime, job satisfaction, tenure, and employee attrition.

## Data Preparation

The `data_cleaning.ipynb` notebook contains the data cleaning and preparation process. The dataset is checked for missing values, duplicate records, data types, and constant features. Selected categorical variables are also encoded for analysis and machine learning.

The cleaned dataset is saved as:

    data/clean/cleaned_data.csv

## Tools & Python Libraries

- Python 3.11
- Pandas
- NumPy
- Statsmodels
- Scikit-learn
- PyCaret 3.3.2
- Matplotlib
- Seaborn
- Microsoft Excel

## Project Status

- [x] Data cleaning and preparation
- [ ] Exploratory data analysis
- [ ] Statistical analysis
- [ ] Data visualization
- [ ] Classification model development and comparison
- [ ] Final model evaluation
- [ ] Save final model
- [ ] Excel Dashboard