# MLOps Experiment 1: Agile and Scrum Demonstration

An end-to-end simulation of Agile and Scrum project management methodologies applied to an MLOps pipeline. This project implements an Iris flower classification system using a Decision Tree Classifier, accompanied by a complete suite of Scrum ceremonies, backlog tracking, automated unit testing, and GitHub Actions CI/CD workflow managed via `uv`.

---

## 1. Project Overview

- **Course / Lab:** Machine Learning Operations (MLOps) Lab – Experiment 1
- **Objective:** Demonstrate how cross-functional Scrum teams plan, prioritize, execute, test, and deliver an ML product increment (Iris Decision Tree MVP) within a time-boxed sprint.
- **Model:** `DecisionTreeClassifier` (via `scikit-learn`)
- **Dataset:** Fisher's Iris Dataset (150 samples across 3 classes: Setosa, Versicolor, Virginica)
- **Environment & Dependency Manager:** `uv`
- **CI/CD Platform:** GitHub Actions (`.github/workflows/tests.yml`)
- **Testing Framework:** Python Standard Library `unittest`

---

## 2. Project Directory Structure

```text
Experiment_1_Agile_Scrum_Demo/
├── .github/
│   └── workflows/
│       └── tests.yml            # GitHub Actions CI workflow (testing & pipeline check)
├── .venv/                       # Project-isolated virtual environment (managed by uv)
├── .gitignore                   # Git ignore file (excludes .venv and caches)
├── data/
│   └── README.md                # Information regarding the Iris dataset
├── docs/
│   ├── Accuracy_Report.md       # Empirical evaluation, test size, and metrics
│   ├── Daily_Scrum.md           # Simulated daily standup meeting responses
│   ├── Sprint_Planning.md       # Sprint goal, backlog task selection, estimates
│   ├── Sprint_Retrospective.md  # Retrospective: successes, challenges, improvements
│   └── Sprint_Review.md         # Deliverables review, demo, and goal achievement
├── models/
│   └── iris_model.pkl           # Trained Decision Tree model binary (serialized)
├── src/
│   └── iris_demo.py             # Main end-to-end training and evaluation script
├── tests/
│   ├── __init__.py              # Tests package initializer
│   └── test_model.py            # Automated unit tests for model artifact and inference
├── pyproject.toml               # Project metadata and dependencies (scikit-learn)
├── uv.lock                      # Exact locked dependencies for reproducibility
├── Product_Backlog.md           # Prioritized user stories (US1 to US6) and rationale
└── README.md                    # Project documentation and execution instructions
```

---

## 3. Prerequisites & Environment Setup with `uv`

### Prerequisites
- macOS / Linux / Windows
- `uv` installed (`uv --version`)
- Python 3.9+ (CPython)

### Setup Instructions (macOS)

1. **Navigate to the Experiment Directory:**
   ```bash
   cd "/Users/adilsyed/Developer/Machine Learning/MLOps/Experiment_1_Agile_Scrum_Demo"
   ```

2. **Create Project Virtual Environment (if not already created):**
   ```bash
   uv venv
   ```
   *This creates an isolated `.venv` inside `Experiment_1_Agile_Scrum_Demo`.*

3. **Install and Sync Dependencies:**
   ```bash
   uv sync
   ```
   *This resolves, locks, and synchronizes dependencies (`scikit-learn` and its sub-dependencies) from `pyproject.toml` into `.venv` using `uv.lock`.*

---

## 4. How to Run the Model

### Option A: Direct Execution with `uv run` (Recommended)
You do not need to manually activate the virtual environment. Simply execute:

```bash
uv run python src/iris_demo.py
```

### Option B: Activated Shell Execution
Alternatively, activate the environment shell first:

```bash
source .venv/bin/activate
python src/iris_demo.py
```

### Verifying Model Loading & Predictions
To verify that the saved model artifact (`models/iris_model.pkl`) loads and performs inference:

```bash
uv run python -c "import pickle; m = pickle.load(open('models/iris_model.pkl', 'rb')); print('Model loaded:', type(m)); print('Sample prediction:', m.predict([[5.1, 3.5, 1.4, 0.2]]))"
```

---

## 5. Automated Testing Workflow

The project uses Python's `unittest` framework to validate model serialization and inference robustness.

To execute the test suite locally:

```bash
uv run python -m unittest discover -s tests -v
```

### What the Unit Tests Verify:
1. **Model Artifact Persistence (`test_01_model_artifact_exists`):** Confirms `models/iris_model.pkl` exists on disk and is non-empty.
2. **Estimator Class Type (`test_02_model_instance_type`):** Confirms unpickled object is an instance of `DecisionTreeClassifier`.
3. **Feature Dimensionality (`test_03_expected_feature_count`):** Confirms the model expects exactly 4 continuous features.
4. **Single-Sample Inference (`test_04_single_sample_prediction`):** Validates scalar prediction format and valid class label ($0, 1, 2$).
5. **Batch Inference (`test_05_batch_prediction_shape_and_classes`):** Validates vector predictions matching input batch size.
6. **Probability Distribution (`test_06_predict_proba_distribution`):** Verifies prediction probabilities sum to $1.0$.
7. **Input Validation & Error Handling (`test_07_invalid_feature_dimension_raises_error`):** Confirms that inputs with incorrect dimensions correctly raise an exception.

---

## 6. Continuous Integration (GitHub Actions)

A CI workflow is defined in `.github/workflows/tests.yml` to automatically validate changes:
- **Triggers:** Pushes to `main` and Pull Requests targeting `main`.
- **Runner:** `ubuntu-latest`.
- **Steps:**
  1. Checks out repository code.
  2. Sets up Python and `uv` using official `astral-sh/setup-uv@v5`.
  3. Syncs dependencies reproducibly using `uv sync`.
  4. Executes the training script (`uv run python src/iris_demo.py`).
  5. Executes the full unit test suite (`uv run python -m unittest discover -s tests -v`).

---

## 7. Execution Pipeline & Output

When executed, `src/iris_demo.py` performs the following steps:
1. **Loads Dataset:** Ingests the 150-sample Iris dataset with 4 continuous features (`sepal length`, `sepal width`, `petal length`, `petal width`).
2. **Splits Data:** Partitions data into 80% train (120 samples) and 20% test (30 samples) using `random_state=42`.
3. **Trains Model:** Fits a `DecisionTreeClassifier(random_state=42)` on the training split.
4. **Evaluates Performance:** Computes classification metrics on the holdout test set:
   - **Test Accuracy:** **100.00%** (1.0000)
   - **Precision / Recall / F1:** 1.00 across all classes
   - **Confusion Matrix:**
     ```text
     [[10,  0,  0],
      [ 0,  9,  0],
      [ 0,  0, 11]]
     ```
5. **Persists Artifact:** Serializes and saves the trained model to `models/iris_model.pkl`.

---

## 8. Scrum & Agile Documentation Index

| Document | Purpose |
| :--- | :--- |
| [Product_Backlog.md](Product_Backlog.md) | Six prioritized user stories (US1–US6) with effort estimates and prioritization rationale. |
| [docs/Sprint_Planning.md](docs/Sprint_Planning.md) | One-week sprint plan, sprint goal, breakdown into tasks, and time estimates. |
| [docs/Daily_Scrum.md](docs/Daily_Scrum.md) | Simulated daily standup responses (Yesterday / Today / Blockers) across 5 Scrum roles. |
| [docs/Sprint_Review.md](docs/Sprint_Review.md) | Demonstration of deliverables, actual model accuracy, and sprint goal completion status. |
| [docs/Sprint_Retrospective.md](docs/Sprint_Retrospective.md) | Post-sprint analysis: successes, environment bottlenecks, and actionable improvements. |
| [docs/Accuracy_Report.md](docs/Accuracy_Report.md) | Empirical evaluation analysis, sample sizes, classification report, and observations. |

---

## 9. Submission Checklist

- [x] Project environment and dependency management powered by `uv` (`pyproject.toml`, `uv.lock`).
- [x] Local virtual environment configured in `.venv/` (isolated from parent directories).
- [x] `.gitignore` created to exclude `.venv/` while tracking source, docs, and model artifacts.
- [x] Decision tree script executed cleanly with `uv run python src/iris_demo.py`.
- [x] Model trained with `random_state=42` and 80/20 train-test split.
- [x] Model artifact serialized and saved in `models/iris_model.pkl`.
- [x] Automated unit test suite implemented in `tests/test_model.py` and passing.
- [x] GitHub Actions workflow configured in `.github/workflows/tests.yml`.
- [x] Empirical accuracy matches actual execution (100.00%).
- [x] Simulated Scrum ceremonies clearly distinguished from code execution.
