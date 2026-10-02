import pandas as pd
from sklearn.model_selection import train_test_split

NUMERIC = ["R&D Spend", "Administration", "Marketing Spend"]


def load_data(path="../data/50_Startups.csv"):
    return pd.read_csv(path)


def split(df, features=NUMERIC):
    X = df[features]
    y = df["Profit"]
    return train_test_split(X, y, test_size=0.2, random_state=42)