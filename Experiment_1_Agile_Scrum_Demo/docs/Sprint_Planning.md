# Sprint Planning Meeting

> **Notice:** This document records the simulated Sprint Planning meeting conducted for **Sprint 1** of the MLOps Iris Classification Project (Experiment 1).

---

## 1. Sprint Overview

- **Sprint Name:** Sprint 1 – Iris Decision Tree MVP
- **Sprint Duration:** 1 Week (5 Working Days: Monday to Friday)
- **Scrum Team Members:**
  - Product Owner (PO)
  - Scrum Master (SM)
  - Data Engineer (DE)
  - Machine Learning Engineer (MLE)
  - Quality Assurance / Tester (QA)
- **Total Team Capacity:** 18 Story Points (approx. 40 person-hours)

---

## 2. Sprint Goal

> **Sprint Goal:**  
> *"Deliver an end-to-end, tested baseline Machine Learning pipeline that classifies Iris flower species using a Decision Tree model, validates its accuracy on an unseen test set, persists the trained artifact for deployment, and produces comprehensive documentation for university submission."*

---

## 3. Selected Sprint Backlog Tasks & Effort Estimation

The team selected all six user stories from the Product Backlog, breaking them down into specific technical tasks and estimating completion times:

| Task ID | User Story | Task Description | Assigned Role | Estimated Time | Story Points |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1.1** | US1: Download Iris Dataset | Verify dataset availability via scikit-learn built-in loader (`load_iris()`) and confirm 150 instances with 4 features. | Data Engineer | 2 Hours | 2 |
| **T1.2** | US2: Clean Dataset | Validate absence of null/NaN values, inspect data types, and prepare 80/20 train-test split with fixed `random_state=42`. | Data Engineer | 3 Hours | 3 |
| **T1.3** | US3: Train Decision Tree Model | Implement `DecisionTreeClassifier` training script in `src/iris_demo.py` using reproducible random seed (`random_state=42`). | ML Engineer | 6 Hours | 5 |
| **T1.4** | US4: Evaluate Accuracy | Run test evaluation against 20% holdout split (30 samples); generate accuracy metric, precision/recall report, and confusion matrix. | Tester / ML Engineer | 4 Hours | 3 |
| **T1.5** | US5: Save Model | Integrate serialization logic to export the trained model as `models/iris_model.pkl` using Python's `pickle` library. | ML Engineer | 3 Hours | 2 |
| **T1.6** | US6: Prepare Documentation | Write Sprint reports (`Sprint_Planning`, `Daily_Scrum`, `Sprint_Review`, `Sprint_Retrospective`, `Accuracy_Report`, and project `README.md`). | Scrum Master / Team | 6 Hours | 3 |
| **Total** | | | | **24 Hours** | **18 Points** |

---

## 4. Definition of Done (DoD)

A task or user story is considered **Done** only when:
1. Python code adheres to PEP 8 standards and runs with zero execution errors.
2. The model trains deterministically using `random_state=42`.
3. Model accuracy and evaluation metrics are computed on the 20% test partition and printed to stdout.
4. Serialized binary `models/iris_model.pkl` is verified to exist on disk and is loadable.
5. All accompanying documentation and sprint artifacts are completed and reviewed.
