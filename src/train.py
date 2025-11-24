import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib   # for saving the trained model


def train_model(features_csv: str, model_out: str = "outputs/fake_news_model.pkl"):
    """
    Train a Random Forest classifier on the extracted features.

    Parameters
    ----------
    features_csv : str
        Path to the CSV file containing features + label column.
    model_out : str
        File path to save the trained model.

    Returns
    -------
    model : RandomForestClassifier
        The trained RandomForest model.
    """
    if not os.path.exists(features_csv):
        raise FileNotFoundError(f"Features file not found: {features_csv}")

    # Load features
    df = pd.read_csv(features_csv)
    print(f"✅ Loaded dataset: {df.shape[0]} samples, {df.shape[1]} columns")

    if 'label' not in df.columns:
        raise ValueError("The dataset must contain a 'label' column.")

    # Separate features and labels
    X = df.drop(columns=['label'])
    y = df['label']

    print("Feature columns:", list(X.columns))
    print("Class distribution:\n", y.value_counts())

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )
    print(f"Training on {X_train.shape[0]} samples, testing on {X_test.shape[0]} samples")

    # Model training
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    # Predictions & evaluation
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print("\n🔎 Classification Report:")
    print(classification_report(y_test, preds))
    print(f"Overall Accuracy: {acc:.4f}")

    # Save the trained model
    os.makedirs(os.path.dirname(model_out), exist_ok=True)
    joblib.dump(model, model_out)
    print(f"💾 Model saved to: {model_out}")

    return model


if __name__ == "__main__":
    # Run training when executed as a script
    model_path = "outputs/fake_news_model.pkl"
    features_path = "outputs/features.csv"
    train_model(features_csv=features_path, model_out=model_path)
