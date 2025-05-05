# main.py
from scripts.train_model import train_model
from scripts.detect_anomaly import predict_url

def main():
    print("1. Train Model")
    print("2. Predict a URL")
    choice = input("Choose option (1/2): ")

    if choice == '1':
        train_model('data/phishing_site_urls.csv')
    elif choice == '2':
        url = input("Enter a URL to test: ")
        result = predict_url(url)
        print(f"\nPrediction: {result}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
