# scripts/detect_anomaly.py
import joblib

def predict_url(url):
    model = joblib.load('models/phishing_detector.pkl')
    prediction = model.predict([url])
    
    return "Phishing" if prediction[0] == 1 else "Legitimate"

if __name__ == "__main__":
    test_url = input("Enter a URL to test: ")
    result = predict_url(test_url)
    print(f"The entered URL is: {result}")
