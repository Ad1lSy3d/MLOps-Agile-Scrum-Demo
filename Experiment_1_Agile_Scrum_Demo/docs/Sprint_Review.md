# Sprint Review Meeting Report

> **Notice:** This document summarizes the simulated Sprint Review conducted at the end of Sprint 1 for **Experiment 1 – Agile and Scrum Demo**.

---

## 1. Meeting Overview
- **Sprint:** Sprint 1 – Iris Decision Tree MVP
- **Sprint Duration:** 1 Week
- **Attendees:** Product Owner, Scrum Master, ML Engineer, Data Engineer, QA Tester, Stakeholders (Lab Instructor / Academic Evaluator)
- **Primary Objective:** Demonstrate the completed product increments, verify acceptance criteria against the Definition of Done, and gather stakeholder feedback.

---

## 2. Sprint Goal Evaluation

- **Sprint Goal:**  
  *"Deliver an end-to-end, tested baseline Machine Learning pipeline that classifies Iris flower species using a Decision Tree model, validates its accuracy on an unseen test set, persists the trained artifact for deployment, and produces comprehensive documentation for university submission."*
- **Sprint Goal Status:** **ACHIEVED** (100% of planned backlog items satisfied).

---

## 3. Deliverables Summary

| User Story | Deliverable Artifact | Verification / Acceptance Status |
| :--- | :--- | :--- |
| **US1 & US2** | Ingestion & Data Preparation logic in `src/iris_demo.py` & `data/README.md` | **Accepted:** Pre-cleaned Iris dataset (150 rows, 4 features) verified via scikit-learn built-in loader; split 80% train (120) and 20% test (30) with `random_state=42`. |
| **US3** | Training Pipeline (`src/iris_demo.py`) | **Accepted:** Decision Tree Classifier trained deterministically on 120 samples. |
| **US4** | Evaluation Report (`docs/Accuracy_Report.md`) | **Accepted:** Holdout test set evaluated with precision, recall, F1, and confusion matrix. |
| **US5** | Model Artifact (`models/iris_model.pkl`) | **Accepted:** Serialized pickle binary created (size: ~2.8 KB) and loadable. |
| **US6** | Comprehensive Documentation | **Accepted:** Product Backlog, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, and README completed. |

---

## 4. Actual Model Performance Demonstration

During the live demonstration of `src/iris_demo.py`, the following actual execution metrics were verified:

- **Split Ratio:** 80% Training (120 samples) / 20% Testing (30 samples)
- **Random Seed:** `random_state=42`
- **Actual Test Accuracy:** **1.0000 (100.00%)**
- **Test Class Distribution:**
  - Iris setosa: 10 samples
  - Iris versicolor: 9 samples
  - Iris virginica: 11 samples
- **Confusion Matrix:**
  ```
  [[10,  0,  0],
   [ 0,  9,  0],
   [ 0,  0, 11]]
  ```
- **Observations:** All 30 test samples were classified correctly. Because the Iris dataset exhibits strong feature separability (particularly petal length and width) and the test sample size is 30, the decision tree achieved perfect classification on this specific partition.

---

## 5. Stakeholder Feedback & Next Steps
- **Stakeholder Acceptance:** The Product Owner accepted all 6 user stories as meeting the Definition of Done.
- **Future Considerations for Subsequent Sprints (Backlog Refinement):**
  - Implement hyperparameter tuning (e.g., `max_depth` restrictions to prevent potential overfitting on larger datasets).
  - Add cross-validation (k-fold) to assess variance across multiple splits.
  - Explore automated CI/CD pipeline integration for retraining upon new data arrivals.
