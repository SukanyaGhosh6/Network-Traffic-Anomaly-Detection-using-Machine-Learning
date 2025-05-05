# scripts/preprocess.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(csv_path):
    # Load the CSV
    df = pd.read_csv(csv_path)

    # Clean null values if any
    df = df.dropna()

    # Label encode the target variable ('label')
    le = LabelEncoder()
    df['label_encoded'] = le.fit_transform(df['label'])

    # Drop columns we don't need (we'll drop raw text label for now)
    X = df['url']
    y = df['label_encoded']

    return X, y, le
