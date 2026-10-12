# Daily Scrum Meeting Standup

> **Disclaimer:** The following entries represent **simulated meeting responses** recorded during a standup session for the Iris Flower Classification project (Sprint 1, Day 3). They illustrate how cross-functional Scrum team members synchronize progress, outline upcoming tasks, and highlight blockers in an MLOps project.

---

## Meeting Details
- **Date:** Simulated Sprint Day 3 (Wednesday)
- **Time:** 09:30 AM – 09:45 AM (15-minute timebox)
- **Facilitator:** Scrum Master
- **Format:** Three standard questions:
  1. *What did you do yesterday?*
  2. *What will you do today?*
  3. *Are there any blockers preventing progress?*

---

## Simulated Standup Responses

### 1. Product Owner (PO)
- **Yesterday:** Reviewed and finalized user stories US1 through US6 in the Product Backlog. Clarified acceptance criteria for model serialization and reporting with academic rubric requirements.
- **Today:** Monitor the pipeline deliverables to ensure the Sprint Goal is tracking toward completion; review the drafted documentation templates.
- **Blockers:** None.

---

### 2. Scrum Master (SM)
- **Yesterday:** Facilitated Sprint Planning, assisted the team in sizing story points, set up the project folder structure, and confirmed Definition of Done criteria.
- **Today:** Ensure the team remains unblocked on environment dependencies; coordinate handover between Data Engineer, ML Engineer, and Tester.
- **Blockers:** None. Need to ensure Python virtual environment dependencies (specifically scikit-learn) are accessible to all team members without disrupting existing environments.

---

### 3. Data Engineer (DE)
- **Yesterday:** Inspected the Iris dataset using scikit-learn's built-in loader (`load_iris()`). Confirmed 150 total records (50 per class) with no missing or corrupted values. Implemented the 80/20 train/test split utilizing `random_state=42`.
- **Today:** Hand over the validated data split arrays (`X_train`, `X_test`, `y_train`, `y_test`) to the ML Engineer; create documentation in `data/` detailing dataset characteristics.
- **Blockers:** None. (Note: Utilizing scikit-learn's built-in dataset resolved the potential blocker of external HTTP downloads and uncleaned raw CSV parsing).

---

### 4. Machine Learning Engineer (MLE)
- **Yesterday:** Implemented the baseline `DecisionTreeClassifier(random_state=42)` in `src/iris_demo.py` and fitted the model against the 120 training samples.
- **Today:** Finalize the model serialization step using `pickle` to export `models/iris_model.pkl`; collaborate with the Tester to verify reproducible inference.
- **Blockers:** None. The decision tree trains deterministically and instantly on local hardware.

---

### 5. Quality Assurance / Tester (QA)
- **Yesterday:** Drafted the test evaluation suite to calculate test accuracy, precision, recall, F1-score, and confusion matrix on the 30-sample holdout test set.
- **Today:** Execute `src/iris_demo.py`, record the exact accuracy and confusion matrix metrics, and document empirical results in `Accuracy_Report.md`.
- **Blockers:** None. Verified that the test script executes cleanly end-to-end and creates the serialized `.pkl` artifact.

---

## Scrum Master Summary
All roles are on schedule. The team has progressed smoothly from data preparation to model training and testing. With no active blockers, Sprint 1 is projected to meet its Sprint Goal ahead of the Sprint Review.
