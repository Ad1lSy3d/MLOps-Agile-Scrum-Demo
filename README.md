# MLOps Laboratory Repository

A centralized collection of laboratory experiments and practical implementations for Machine Learning Operations (MLOps). Each experiment is maintained in its own dedicated, self-contained directory containing project configuration, source code, tests, documentation, and dependencies.

---

## Laboratory Experiments

| Experiment | Title | Description | Status |
| :--- | :--- | :--- | :--- |
| **Experiment 1** | [Agile and Scrum Demo](Experiment_1_Agile_Scrum_Demo/README.md) | End-to-end simulation of Agile & Scrum project management for an ML pipeline (Iris flower classification with Decision Trees, automated unit tests, and GitHub Actions CI). | **Completed** |
| *Future Experiments* | *Upcoming Laboratories* | Subsequent MLOps modules (e.g., CI/CD pipelines, containerization, tracking, and deployment). | *Planned* |

---

## Repository Structure

```text
MLOps/
├── .github/
│   └── workflows/
│       └── tests.yml                     # Root CI workflow for automated testing
├── .gitignore                            # Root ignore rules (.venv, caches)
├── README.md                             # Repository overview and experiment index
└── Experiment_1_Agile_Scrum_Demo/        # Experiment 1: Agile & Scrum Implementation
    ├── .github/
    │   └── workflows/
    │       └── tests.yml                 # Experiment 1 workflow specification
    ├── data/
    │   └── README.md                     # Dataset documentation
    ├── docs/                             # Scrum artifacts and reports
    │   ├── Accuracy_Report.md
    │   ├── Daily_Scrum.md
    │   ├── Sprint_Planning.md
    │   ├── Sprint_Retrospective.md
    │   └── Sprint_Review.md
    ├── models/
    │   └── iris_model.pkl                # Trained model artifact
    ├── src/
    │   └── iris_demo.py                  # Model training and evaluation script
    ├── tests/                            # Automated unit tests
    │   ├── __init__.py
    │   └── test_model.py
    ├── .gitignore                        # Experiment-level gitignore
    ├── Product_Backlog.md                # Prioritized Scrum backlog
    ├── pyproject.toml                    # Project configuration and dependencies
    ├── README.md                         # Detailed Experiment 1 documentation
    └── uv.lock                           # Locked dependency graph
```

---

## Quick Start

To run an experiment, navigate to its respective directory:

```bash
# Navigate to Experiment 1
cd Experiment_1_Agile_Scrum_Demo

# Sync dependencies using uv
uv sync

# Run the training pipeline
uv run python src/iris_demo.py

# Execute the test suite
uv run python -m unittest discover -s tests -v
```

For full details, please refer to the dedicated [Experiment 1 Documentation](Experiment_1_Agile_Scrum_Demo/README.md).
