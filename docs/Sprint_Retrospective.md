# Sprint Retrospective Meeting Report

> **Notice:** This document records the simulated Sprint Retrospective held following Sprint 1 of **Experiment 1 – Agile and Scrum Demo**.

---

## 1. Meeting Details
- **Sprint:** Sprint 1 – Iris Decision Tree MVP
- **Facilitator:** Scrum Master
- **Participants:** Product Owner, Scrum Master, ML Engineer, Data Engineer, QA Tester
- **Format:** Agile Retrospective Framework (What Went Well, Problems Encountered / Challenges, Proposed Actionable Improvements)

---

## 2. What Went Well (Successes)

1. **Clear Prioritization:**
   - Establishing strict dependencies (data preparation and model training prioritized first) prevented idle time between team roles.
2. **Deterministic Reproducibility:**
   - Pinning `random_state=42` across the train-test split and Decision Tree classifier ensured 100% reproducible execution results across environments.
3. **Zero External Dependency Friction:**
   - Utilizing `scikit-learn`'s built-in Iris dataset avoided external network fetch failures and complex parsing bugs during the initial baseline sprint.
4. **Clean Project Modularization:**
   - Separating `src/` (logic), `models/` (artifacts), `docs/` (Scrum artifacts), and `data/` provided a maintainable and clean repository structure aligned with MLOps conventions.

---

## 3. Problems Encountered (Challenges & Bottlenecks)

1. **Environment & Dependency Mismatch:**
   - **Challenge:** The host system Python environment (`/opt/homebrew/bin/python3`) did not have `scikit-learn` pre-installed globally.
   - **Resolution:** The team identified and leveraged an existing local Python virtual environment rather than making destructive global modifications or uncoordinated package installations.
2. **Risk of Overconfidence from 100% Test Accuracy:**
   - **Challenge:** The decision tree achieved 100% test accuracy on the 30-sample holdout set. In machine learning, a small test sample and unconstrained decision trees carry the risk of overestimating real-world generalization or masking overfitting.
   - **Resolution:** Acknowledged the need for K-Fold cross-validation in future iterations to ensure scientific rigor.
3. **Simulating Real-World Data Engineering:**
   - **Challenge:** Because the built-in Iris dataset is already pre-cleaned and standardized, real-world data engineering tasks (handling null values, categorical encoding, outlier clipping) were not exercised.

---

## 4. Proposed Improvements (Action Items for Sprint 2)

| Action Item | Description | Owner | Priority |
| :--- | :--- | :--- | :--- |
| **A1: Requirements Specification** | Provide a lightweight `requirements.txt` documenting exact package versions (`scikit-learn`, `numpy`) for consistent setup across machines. | Scrum Master / MLE | High |
| **A2: K-Fold Cross Validation** | Incorporate 5-fold cross-validation in `src/` to report mean accuracy and standard deviation across data splits. | QA Tester / MLE | Medium |
| **A3: Automated Inference Script** | Create an evaluation/prediction script `predict.py` that loads `models/iris_model.pkl` to score new user-provided feature inputs. | ML Engineer | Medium |
| **A4: Decision Tree Pruning** | Experiment with `max_depth` and `min_samples_split` hyperparameter limits to understand model pruning and feature importance. | ML Engineer | Low |
