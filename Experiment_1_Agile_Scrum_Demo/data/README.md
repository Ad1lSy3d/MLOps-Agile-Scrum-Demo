# Data Directory

This directory is designated for project datasets in the MLOps pipeline.

## Dataset Information
For this lab experiment (**Experiment 1: Agile and Scrum Demo**), the standard benchmark **Iris dataset** is loaded directly via `scikit-learn.datasets.load_iris()`.

### Notes:
- **No manual downloading or cleaning required:** Scikit-learn's built-in Iris dataset contains all 150 instances (4 numerical features: sepal length, sepal width, petal length, petal width) formatted and cleaned without missing values.
- In subsequent lab experiments with raw external datasets, raw data files (`.csv`, `.parquet`, etc.) can be placed here.
