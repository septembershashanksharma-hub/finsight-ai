import pandas as pd

def load_clean_data(filepath):
    return pd.read_csv(filepath)


def get_default_rate_by_grade(df):
    return df.groupby(df['grade'])['is_default'].mean() * 100

