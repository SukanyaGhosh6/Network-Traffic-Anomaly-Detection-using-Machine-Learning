# scripts/train_model.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from preprocess import load_and_preprocess

def train_model(csv_path):
    X, y, le = load_and_preprocess(csv_path)

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create pipeline
    pipeline = make_pipeline(
        TfidfVectorizer(),
        RandomForestClassifier(n_estimators=100, random_state=42)
    )

    # Train model
    pipeline.fit(X_train, y_train)

    # Evaluate
    y_pred = pipeline.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save the model
    joblib.dump(pipeline, 'models/phishing_detector.pkl')
    print("Model saved to models/phishing_detector.pkl")

if __name__ == "__main__":
    train_model('data/phishing_site_urls.csv')  # <-- update path if needed
