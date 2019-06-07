import pandas as pd


def read(filename='result.zip'):
    """Reads the file received in the parameter. File must be a zip."""
    df = pd.read_csv(filename, compression='zip', low_memory=False)
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')
    return df
