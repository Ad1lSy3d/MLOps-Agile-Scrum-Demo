"""
Iris Flower Classification - Decision Tree Demo
Experiment 1: Agile and Scrum Demo (MLOps Lab)

This script demonstrates a basic MLOps machine learning pipeline:
1. Loads the built-in Iris dataset from scikit-learn (pre-cleaned benchmark dataset).
2. Splits data into 80% training and 20% testing sets (random_state=42).
3. Trains a DecisionTreeClassifier.
4. Evaluates model performance (Accuracy, Classification Report, Confusion Matrix).
5. Serializes and saves the trained model to 'models/iris_model.pkl'.
"""

import os
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def main():
    # Define project root directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    models_dir = os.path.join(project_root, "models")
    os.makedirs(models_dir, exist_ok=True)
    model_save_path = os.path.join(models_dir, "iris_model.pkl")

    print("=" * 60)
    print("  Iris Flower Classification - Agile / MLOps Demo")
    print("=" * 60)

    # Step 1: Load Dataset
    print("\n[Step 1] Loading Iris dataset from scikit-learn...")
    iris = load_iris()
    X, y = iris.data, iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    print(f"Total samples: {X.shape[0]}, Features: {X.shape[1]}")
    print(f"Features: {list(feature_names)}")
    print(f"Classes: {list(target_names)}")

    # Step 2: Train-Test Split (80% Train, 20% Test)
    print("\n[Step 2] Splitting dataset (80% train, 20% test, random_state=42)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples:  {X_test.shape[0]}")

    # Step 3: Train Model
    print("\n[Step 3] Training DecisionTreeClassifier...")
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    print("Model training complete.")

    # Step 4: Model Evaluation
    print("\n[Step 4] Evaluating model on the test set...")
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_pct = accuracy * 100

    print(f"Accuracy: {accuracy:.4f} ({accuracy_pct:.2f}%)")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Step 5: Save Model Artifact
    print(f"\n[Step 5] Saving model to: {model_save_path}")
    with open(model_save_path, "wb") as f:
        pickle.dump(clf, f)

    if os.path.exists(model_save_path):
        file_size = os.path.getsize(model_save_path)
        print(f"Model saved successfully ({file_size} bytes).")
    else:
        print("ERROR: Model file was not created.")

    print("\n" + "=" * 60)
    print("  Execution Finished Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()
