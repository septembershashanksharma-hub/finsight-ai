def load_clean_data(filepath):
    import pandas as pd
    return pd.read_csv(filepath)


def get_default_rate_by_grade(df):
    