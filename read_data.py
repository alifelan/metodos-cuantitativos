import pandas as pd


def read(filename):
    """Reads the file received in the parameter. File must be a zip."""
    df = pd.read_csv(filename, compression='zip')
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    return df
