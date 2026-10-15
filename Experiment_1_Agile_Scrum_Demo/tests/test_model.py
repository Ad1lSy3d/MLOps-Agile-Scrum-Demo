"""
Automated unit tests for the trained Iris Decision Tree model.

Validates:
1. Presence of the persisted model artifact.
2. Successful model deserialization.
3. Model attribute verification (estimator type, feature expectations).
4. Prediction validity (output shape, valid class label outputs).
5. Robustness against invalid inputs (e.g. incorrect feature count).
"""

import os
import pickle
import unittest
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris


class TestIrisModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Resolve project root relative to tests directory
        test_dir = os.path.dirname(os.path.abspath(__file__))
        cls.project_root = os.path.dirname(test_dir)
        cls.model_path = os.path.join(cls.project_root, "models", "iris_model.pkl")

        # Ensure the model exists before running assertions; if missing, train it
        if not os.path.exists(cls.model_path):
            import subprocess
            subprocess.run(
                ["python", os.path.join(cls.project_root, "src", "iris_demo.py")],
                check=True,
            )

        with open(cls.model_path, "rb") as f:
            cls.model = pickle.load(f)

    def test_01_model_artifact_exists(self):
        """Verify that the model file exists and is non-empty."""
        self.assertTrue(os.path.exists(self.model_path), "Model artifact does not exist.")
        self.assertGreater(os.path.getsize(self.model_path), 0, "Model artifact is empty.")

    def test_02_model_instance_type(self):
        """Verify that deserialized object is a scikit-learn DecisionTreeClassifier."""
        self.assertIsInstance(
            self.model,
            DecisionTreeClassifier,
            "Loaded model is not a DecisionTreeClassifier.",
        )

    def test_03_expected_feature_count(self):
        """Verify model expects 4 input features corresponding to the Iris dataset."""
        self.assertEqual(
            self.model.n_features_in_,
            4,
            f"Expected 4 features, but model expects {self.model.n_features_in_}.",
        )

    def test_04_single_sample_prediction(self):
        """Verify single input sample prediction shape and valid class ID."""
        sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # Typical Iris-setosa
        prediction = self.model.predict(sample)

        self.assertEqual(len(prediction), 1, "Expected single prediction output.")
        self.assertIn(
            prediction[0],
            [0, 1, 2],
            f"Prediction {prediction[0]} is not in valid class set [0, 1, 2].",
        )

    def test_05_batch_prediction_shape_and_classes(self):
        """Verify batch prediction returns matching length with valid species labels."""
        batch_samples = np.array([
            [5.1, 3.5, 1.4, 0.2],  # Setosa
            [6.0, 2.9, 4.5, 1.5],  # Versicolor
            [6.9, 3.1, 5.4, 2.1],  # Virginica
        ])
        predictions = self.model.predict(batch_samples)

        self.assertEqual(len(predictions), 3, "Output prediction length mismatch.")
        for p in predictions:
            self.assertIn(p, [0, 1, 2], f"Invalid class label {p} returned.")

    def test_06_predict_proba_distribution(self):
        """Verify predict_proba outputs valid probability distributions summing to 1."""
        sample = np.array([[5.8, 2.7, 4.1, 1.0]])
        probabilities = self.model.predict_proba(sample)

        self.assertEqual(probabilities.shape, (1, 3), "Probability matrix shape mismatch.")
        self.assertAlmostEqual(
            float(np.sum(probabilities)),
            1.0,
            places=5,
            msg="Probabilities do not sum to 1.0.",
        )

    def test_07_invalid_feature_dimension_raises_error(self):
        """Verify model rejects input with incorrect feature count."""
        invalid_sample = np.array([[5.1, 3.5]])  # 2 features instead of 4
        with self.assertRaises((ValueError, Exception)):
            self.model.predict(invalid_sample)


if __name__ == "__main__":
    unittest.main()
