# Experiment 3: GitHub Actions Continuous Integration (CI) Report

---

## 1. Aim and Objectives

### Aim
To configure, execute, and validate an automated Continuous Integration (CI) pipeline using **GitHub Actions** for a Python application with unit testing in **pytest**, demonstrating automated build verification, intentional failure detection, and automated recovery verification.

### Objectives
1. Implement a modular Python calculator application (`app.py`) providing basic arithmetic operations (`add`, `subtract`, `multiply`, `divide`).
2. Implement a comprehensive unit test suite (`test_app.py`) using `pytest` covering normal execution and edge cases (e.g. division by zero).
3. Establish a reproducible Python environment and dependency configuration using `requirements.txt` and `uv`.
4. Configure an automated GitHub Actions CI workflow to trigger on `push` and `pull_request` events to the `main` branch.
5. Demonstrate end-to-end CI pipeline success on the initial implementation.
6. Introduce an intentional local defect into the application logic, observe local unit test failure, commit and push to remote, and verify that the GitHub Actions CI pipeline catches the defect and reports failure.
7. Restore correct application logic, verify passing local unit tests, push the fix, and confirm recovery in GitHub Actions CI.

---

## 2. Software and Tools Required

| Software / Tool | Version / Details | Purpose |
| :--- | :--- | :--- |
| **Operating System** | macOS (Darwin 24.x / Apple Silicon) | Host operating system |
| **Python** | 3.11.15 | Programming language runtime |
| **Package / Environment Manager** | `uv` / `pip` | Project isolation and dependency management |
| **Testing Framework** | `pytest` 9.1.1 | Unit test execution and assertion reporting |
| **Version Control** | Git 2.x | Source control management and commit tracking |
| **Remote Repository** | GitHub (`Ad1lSy3d/MLOps-Agile-Scrum-Demo`) | Remote code hosting and collaboration |
| **CI/CD Platform** | GitHub Actions (`ubuntu-latest` runner) | Cloud-based automated testing pipeline |

---

## 3. Project Structure

```text
MLOps/
├── .github/
│   └── workflows/
│       └── tests.yml                                  # Multi-job root GitHub Actions CI workflow
├── README.md                                          # Central repository documentation
├── Experiment_1_Agile_Scrum_Demo/                     # Experiment 1 files
├── Experiment_2_Git_GitHub_CI_CD/                     # Experiment 2 files
└── Experiment_3_GitHub_Actions_CI/                    # Experiment 3 Directory
    ├── .github/
    │   └── workflows/
    │       └── ci.yml                                 # Standalone Experiment 3 workflow specification
    ├── .gitignore                                     # Ignore rules (__pycache__, .pytest_cache)
    ├── app.py                                         # Calculator application source code
    ├── requirements.txt                               # Direct test dependencies (pytest)
    ├── test_app.py                                    # 5 pytest unit test cases
    ├── Experiment_3_Report.md                         # Detailed laboratory report
    └── screenshots/                                   # Evidence repository (18 genuine captures)
        ├── 01_project_structure.png
        ├── 02_app_py.png
        ├── 03_test_app_py.png
        ├── 04_requirements_and_workflow.png
        ├── 05_application_output.png
        ├── 06_initial_tests_passed.png
        ├── 07_git_status_and_branch.png
        ├── 08_git_add_commit_push.png
        ├── 09_git_log_history.png
        ├── 10_initial_ci_success.png
        ├── 11_git_diff_failure.png
        ├── 12_local_test_failure.png
        ├── 13_failure_commit_push.png
        ├── 14_github_actions_failure.png
        ├── 15_local_recovery_tests.png
        ├── 16_git_recovery_commit_push.png
        ├── 17_github_actions_final_success.png
        └── 18_final_git_history.png
```

---

## 4. Application Implementation (`app.py`)

The application implements four core arithmetic functions with proper error handling for invalid operations:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))
```

### Execution Output
```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

---

## 5. Explanation of Unit Tests (`test_app.py`)

The test suite validates function correctness and boundary conditions across 5 distinct test functions:

```python
import pytest
from app import add, subtract, multiply, divide


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

1. **`test_add`**: Verifies standard addition ($10 + 5 = 15$).
2. **`test_subtract`**: Verifies standard subtraction ($10 - 5 = 5$).
3. **`test_multiply`**: Verifies standard multiplication ($10 \times 5 = 50$).
4. **`test_divide`**: Verifies standard division ($10 / 5 = 2.0$).
5. **`test_divide_by_zero`**: Ensures that division by zero raises a `ValueError` as designed, preventing silent unhandled exceptions.

---

## 6. GitHub Actions Workflow Configuration

GitHub Actions discovers workflows located in `.github/workflows/` at the repository root. The root workflow `.github/workflows/tests.yml` contains a dedicated job for Experiment 3:

```yaml
  test-experiment-3:
    name: Run Unit Tests (Experiment 3)
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: Experiment_3_GitHub_Actions_CI

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run application
        run: python app.py

      - name: Run automated tests with pytest
        run: pytest -v test_app.py
```

### Workflow Steps Breakdown
1. **`actions/checkout@v4`**: Fetches repository source code into the runner workspace.
2. **`actions/setup-python@v5`**: Configures CPython 3.11 environment with caching and path resolution.
3. **`Install dependencies`**: Upgrades `pip` and installs required testing libraries (`pytest`) specified in `Experiment_3_GitHub_Actions_CI/requirements.txt`.
4. **`Run application`**: Executes `app.py` in non-interactive mode to verify script integrity.
5. **`Run automated tests with pytest`**: Executes `pytest -v test_app.py`, producing detailed per-test PASS/FAIL logs and setting the overall job exit status code.

---

## 7. Actual Terminal and Git Commands

### Local Execution and Testing Commands
```bash
# Execute application via uv
uv run --project Experiment_3_GitHub_Actions_CI python Experiment_3_GitHub_Actions_CI/app.py

# Run unit tests via uv
uv run --project Experiment_3_GitHub_Actions_CI pytest -v Experiment_3_GitHub_Actions_CI/test_app.py
```

### Git Inspection Commands
```bash
git branch --show-current
git status
git remote -v
git log --oneline --decorate -10
```

---

## 8. CI/CD Lifecycle & Verification Evidence

### Phase 1: Initial Working Implementation (Success)
- **Commit Hash:** `056f94a`
- **Commit Message:** `Implement Experiment 3: GitHub Actions CI with calculator demo and tests`
- **Local Test Result:** 5 passed in 0.01s.
- **GitHub Actions Run ID:** `38870627703`
- **GitHub Actions Run URL:** [https://github.com/Ad1lSy3d/MLOps-Agile-Scrum-Demo/actions/runs/38870627703](https://github.com/Ad1lSy3d/MLOps-Agile-Scrum-Demo/actions/runs/38870627703)
- **Status / Conclusion:** `completed` / **`success`**

### Phase 2: Intentional Local Failure Demonstration (Failure)
- **Defect Introduced:** In `Experiment_3_GitHub_Actions_CI/app.py`, changed line 2 to `return a + b + 1`.
- **Git Diff:**
  ```diff
  --- a/Experiment_3_GitHub_Actions_CI/app.py
  +++ b/Experiment_3_GitHub_Actions_CI/app.py
  @@ -1,5 +1,5 @@
   def add(a, b):
  -    return a + b
  +    return a + b + 1
  ```
- **Local Test Output:**
  ```text
  FAILED Experiment_3_GitHub_Actions_CI/test_app.py::test_add - assert 16 == 15
  1 failed, 4 passed in 0.03s
  ```
- **Commit Hash:** `f7dc83e`
- **Commit Message:** `Demonstrate CI failure with incorrect addition`
- **GitHub Actions Run ID:** `38870989347`
- **GitHub Actions Run URL:** [https://github.com/Ad1lSy3d/MLOps-Agile-Scrum-Demo/actions/runs/38870989347](https://github.com/Ad1lSy3d/MLOps-Agile-Scrum-Demo/actions/runs/38870989347)
- **Status / Conclusion:** `completed` / **`failure`** (Step `Run automated tests with pytest` failed with exit code 1)

### Phase 3: Code Correction and CI Recovery (Success)
- **Fix Applied:** Restored `return a + b` in `Experiment_3_GitHub_Actions_CI/app.py`.
- **Local Test Output:** `5 passed in 0.01s` (100% tests passing).
- **Commit Hash:** `6a36079`
- **Commit Message:** `Fix addition function after CI failure demo`
- **GitHub Actions Run ID:** `38871275884`
- **GitHub Actions Run URL:** [https://github.com/Ad1lSy3d/MLOps-Agile-Scrum-Demo/actions/runs/38871275884](https://github.com/Ad1lSy3d/MLOps-Agile-Scrum-Demo/actions/runs/38871275884)
- **Status / Conclusion:** `completed` / **`success`** (All jobs and steps passed)

---

## 9. Screenshot Evidence Index

All 18 genuine screenshots were captured directly using macOS native window controls (`screencapture`) from Terminal and Safari:

| No. | Screenshot File | Description / Command Shown |
| :---: | :--- | :--- |
| **01** | `01_project_structure.png` | Directory structure of `Experiment_3_GitHub_Actions_CI/` |
| **02** | `02_app_py.png` | Complete source code of `app.py` displayed with line numbers |
| **03** | `03_test_app_py.png` | Complete source code of `test_app.py` with 5 test cases |
| **04** | `04_requirements_and_workflow.png` | Content of `requirements.txt` and `.github/workflows/ci.yml` |
| **05** | `05_application_output.png` | Terminal execution of `uv run python app.py` showing arithmetic output |
| **06** | `06_initial_tests_passed.png` | Initial pytest execution showing `5 passed in 0.01s` |
| **07** | `07_git_status_and_branch.png` | Terminal output of `git branch`, `git status`, and `git remote -v` |
| **08** | `08_git_add_commit_push.png` | Git staging, commit (`056f94a`), and push to `origin/main` |
| **09** | `09_git_log_history.png` | `git log --oneline --decorate -10` prior to failure testing |
| **10** | `10_initial_ci_success.png` | Safari screenshot of successful GitHub Actions Run #5 (`056f94a`) |
| **11** | `11_git_diff_failure.png` | `git diff` showing the intentional defect (`return a + b + 1`) |
| **12** | `12_local_test_failure.png` | Local pytest output showing `test_add FAILED` (`assert 16 == 15`) |
| **13** | `13_failure_commit_push.png` | Git commit (`f7dc83e`) and push of intentional failure |
| **14** | `14_github_actions_failure.png` | Safari screenshot of failed GitHub Actions job showing error log |
| **15** | `15_local_recovery_tests.png` | Local recovery execution: arithmetic output & `5 passed in 0.01s` |
| **16** | `16_git_recovery_commit_push.png` | Git commit (`6a36079`) and push of recovery fix |
| **17** | `17_github_actions_final_success.png` | Safari screenshot of final successful GitHub Actions Run #7 |
| **18** | `18_final_git_history.png` | Complete final `git log --oneline --decorate -10` |

---

## 10. Results and Conclusion

1. **Continuous Integration Demonstrated**: The automated CI workflow correctly detected code pushes to the `main` branch and ran the full suite of unit tests on an isolated Ubuntu runner in GitHub Actions.
2. **Defect Trapping**: When an intentional defect was committed (`f7dc83e`), GitHub Actions immediately blocked the pipeline, reported an exit code 1, and flagged `test_add` failure, demonstrating the protective nature of CI gates against regression errors.
3. **Rapid Feedback & Recovery**: Upon fixing the defect locally and pushing commit `6a36079`, the CI pipeline re-executed automatically and returned to green (`success`), validating end-to-end continuous integration and delivery practices.
