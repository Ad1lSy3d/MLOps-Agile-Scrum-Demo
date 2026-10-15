# Model Accuracy & Evaluation Report

## 1. Overview
This report documents the empirical evaluation results obtained from executing `src/iris_demo.py` on the Iris flower benchmark dataset using scikit-learn's `DecisionTreeClassifier`.

---

## 2. Experimental Setup & Evaluation Method

- **Dataset:** Fisher's Iris Dataset (via `sklearn.datasets.load_iris`)
- **Total Instances:** 150 samples (balanced: 50 Setosa, 50 Versicolor, 50 Virginica)
- **Features (4 continuous numerical measurements in cm):**
  1. Sepal Length
  2. Sepal Width
  3. Petal Length
  4. Petal Width
- **Evaluation Partition:**
  - **Method:** Holdout validation via `sklearn.model_selection.train_test_split`
  - **Train/Test Ratio:** 80% Training / 20% Testing
  - **Training Set Size:** 120 instances
  - **Test Set Size:** 30 instances
  - **Random Seed:** `random_state=42` (ensures exact reproducibility)
- **Model Configuration:**
  - **Algorithm:** `sklearn.tree.DecisionTreeClassifier`
  - **Random Seed:** `random_state=42`
  - **Criterion:** Gini impurity (default)

---

## 3. Empirical Execution Results

### 3.1 Model Accuracy
$$\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Test Predictions}} = \frac{30}{30} = 1.0000 \quad (100.00\%)$$

### 3.2 Detailed Classification Report
| Class Name | Precision | Recall | F1-Score | Support (Sample Count) |
| :--- | :---: | :---: | :---: | :---: |
| **Iris-setosa** | 1.00 | 1.00 | 1.00 | 10 |
| **Iris-versicolor** | 1.00 | 1.00 | 1.00 | 9 |
| **Iris-virginica** | 1.00 | 1.00 | 1.00 | 11 |
| **Accuracy** | | | **1.00** | **30** |
| **Macro Average** | 1.00 | 1.00 | 1.00 | 30 |
| **Weighted Average** | 1.00 | 1.00 | 1.00 | 30 |

### 3.3 Confusion Matrix
$$\begin{pmatrix}
10 & 0 & 0 \\
0 & 9 & 0 \\
0 & 0 & 11
\end{pmatrix}$$

- **Row 1 (True Setosa):** 10 predicted Setosa, 0 Versicolor, 0 Virginica
- **Row 2 (True Versicolor):** 0 predicted Setosa, 9 predicted Versicolor, 0 Virginica
- **Row 3 (True Virginica):** 0 predicted Setosa, 0 Versicolor, 11 predicted Virginica

---

## 4. Key Observations & Analysis

1. **High Separability of Iris Benchmark:**
   - *Iris-setosa* is linearly separable from the other two species purely by petal length and width.
   - *Iris-versicolor* and *Iris-virginica* have near-separable clusters with slight boundary proximity. On this specific 80/20 partition (`random_state=42`), the decision tree was able to place threshold cuts that cleanly separated all test instances.
2. **Impact of Test Sample Size:**
   - The test set consists of 30 samples. While achieving 100% accuracy demonstrates that the model learned effective decision boundaries for this sample, in real-world MLOps scenarios, small test partitions can lead to optimistic performance estimates.
3. **Overfitting Considerations:**
   - An unconstrained decision tree can grow until every training node is pure, creating complex boundaries. For production MLOps systems, techniques like cost-complexity pruning, setting `max_depth`, or utilizing ensemble methods (e.g., Random Forests) together with K-Fold cross-validation are recommended to prevent variance issues.

---

## 5. Artifact Verification
- **Artifact Path:** `models/iris_model.pkl`
- **Serialization Format:** Python `pickle` (binary protocol)
- **Status:** Verified present on disk (size: 2,824 bytes).
