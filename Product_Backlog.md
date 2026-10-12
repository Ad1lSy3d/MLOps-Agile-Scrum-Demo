# Product Backlog: Iris Flower Classification MLOps Project

## Overview
This document represents the simulated Product Backlog for **Experiment 1 – Agile and Scrum Demo**, an MLOps project demonstrating the development and tracking of an Iris flower classification system using Agile and Scrum methodologies.

---

## User Stories and Prioritization

| User Story ID | Title | Description | Priority | Story Points | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **US1** | **Download Iris Dataset** | *As a Data Engineer*, I need to obtain the Iris dataset so that the team has reliable feature data for model development. | **High** | 2 | Completed (Built-in via `scikit-learn`) |
| **US2** | **Clean Dataset** | *As a Data Engineer*, I need to verify data integrity, check for missing values, and structure features and targets so that the model can be trained without data anomalies. | **High** | 3 | Completed (Verified clean built-in data) |
| **US3** | **Train Decision Tree Model** | *As an ML Engineer*, I want to train a `DecisionTreeClassifier` on the training split so that the model learns decision boundaries for classifying Iris species. | **High** | 5 | Completed |
| **US4** | **Evaluate Accuracy** | *As a Tester / ML Engineer*, I want to evaluate the model on an independent test set (20%) and compute accuracy, precision, recall, and a confusion matrix to validate performance. | **Medium** | 3 | Completed |
| **US5** | **Save Model** | *As an MLOps Engineer*, I want to serialize and export the trained model (`iris_model.pkl`) into `models/` so that it can be deployed or reloaded in production pipelines. | **Medium** | 2 | Completed |
| **US6** | **Prepare Documentation** | *As a Scrum Master / Tech Writer*, I need to compile comprehensive project documentation, sprint ceremonies, and reports so that the project meets academic lab standards. | **Low** | 3 | Completed |

---

## Why High-Priority Tasks Come First

In Agile and Scrum frameworks, prioritization ensures maximum value delivery, progressive de-risking, and orderly technical dependency management:

1. **Foundational Technical Dependencies:**
   - Machine learning workflows are strictly sequential. A model cannot be trained without clean data (US1 & US2), and evaluation/persistence cannot happen without a trained model (US3).
   - High-priority items establish the core data and algorithmic pipeline required for any downstream task to function.

2. **Minimum Viable Product (MVP) & Risk Reduction:**
   - High-priority stories validate core project viability early in the Sprint. If data ingestion or algorithm training encounters algorithmic or computational blockers, the team discovers them immediately rather than at the end of the development cycle.

3. **Value-Driven Delivery:**
   - Scrum prioritizes working software over exhaustive documentation. High-priority items directly deliver the primary business logic (data ingestion and training), while secondary operational items (evaluation and serialization) and non-functional requirements (documentation) build upon an already verified foundation.

---

## Technical Implementation Note
> **Transparency Notice:** In a real-world enterprise pipeline, US1 and US2 may involve fetching raw CSV/database records and performing imputation or deduplication. For this educational demonstration, scikit-learn's standard `sklearn.datasets.load_iris()` was utilized. This package provides the benchmark dataset directly within the Python environment in a pre-cleaned, numerical format (150 samples across 4 features, zero missing values), satisfying US1 and US2 without requiring manual external file downloads.
