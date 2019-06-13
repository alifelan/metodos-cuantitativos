import pandas as pd


def filter_df(df: pd.DataFrame = pd.DataFrame()):
    if df.empty:
        print('Reading data...')
        df = read()
    df2 = df.iloc[:, 3:5]
    df2['Speed_limit'] = df['Speed_limit']
    return df2


def read(filename='result.zip'):
    """Reads the file received in the parameter. File must be a zip."""
    df = pd.read_csv(filename, compression='zip', low_memory=False)
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')
    return df
