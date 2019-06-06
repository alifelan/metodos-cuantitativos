import pandas as pd


def read(filename):
    df = pd.read_csv(filename, compression='zip')
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    return df
