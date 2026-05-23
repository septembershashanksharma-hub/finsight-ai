import pandas as pd

def load_clean_data(filepath):
    """
    loads clean CSV, returns DataFrame
    """

    return pd.read_csv(filepath)


def get_default_rate_by_grade(df):
    """
    returns default rate % by grade
    """

    return df.groupby(df['grade'])['is_default'].mean() * 100

def get_default_rate_by_purpose(df):
    """
    returns default rate % by purpose
    """

    return df.groupby(df['purpose'])['is_default'].mean() * 100

def get_high_risk_loans(df, threshold=20):
    """
    returns loans where int_rate is above threshold
    """

    return df[df['int_rate']>threshold]


