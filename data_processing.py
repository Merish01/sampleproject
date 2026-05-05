import pandas as pd

def process_data(df):
    df = df.dropna()

    df['Hours'] = pd.to_numeric(df['Hours'], errors='coerce')
    df['Scores'] = pd.to_numeric(df['Scores'], errors='coerce')

    df['hours_group'] = pd.cut(df['Hours'], bins=5)

    grouped = df.groupby('hours_group')['Scores'].mean()

    return df, grouped