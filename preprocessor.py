import pandas as pd

def load_data(path: str):
    return pd.read_csv(path)

def preprocess(df: pd.DataFrame):
    # Example preprocessing
    df = df.dropna()
    df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek
    return df

