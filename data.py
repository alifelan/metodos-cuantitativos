import pandas as pd
from sklearn import preprocessing


def filter(df: pd.DataFrame = pd.DataFrame()):
    """Returns only important columns"""
    if df.empty:
        df = read()
    df2 = df.iloc[:, 1:3]
    df2['Speed_limit'] = df['Speed_limit']
    return df2


def read(filename='result.zip'):
    """Reads the file received in the parameter. File must be a zip."""
    print('Reading data...')
    df = pd.read_csv(filename, compression='zip', low_memory=False)
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')
    return df


def normalize(df: pd.DataFrame = pd.DataFrame()):
    """Normalizes DataFrame"""
    if df.empty:
        df = filter(read())
    values = df.values
    scaler = preprocessing.MinMaxScaler()
    scaled_values = scaler.fit_transform(values)
    df = pd.DataFrame(scaled_values)
    return df
