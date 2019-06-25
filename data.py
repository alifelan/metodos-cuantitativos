import pandas as pd
import numpy as np
import pickle


def filter(df: pd.DataFrame = pd.DataFrame()):
    """Returns only important columns"""
    if df.empty:
        df = read()
    print('Filtering data...')
    df = df.dropna()
    df2 = pd.DataFrame()
    df2['Location_Easting_OSGR'] = df['Location_Easting_OSGR']
    df2['Location_Northing_OSGR'] = df['Location_Northing_OSGR']
    df2['Month'] = df['Date'].dt.strftime('%m').astype(int)
    df2['Day'] = df['Date'].dt.strftime('%d').astype(int)
    df2['Day_of_Week'] = df['Day_of_Week']
    df2['Time'] = np.array([t.timestamp() for t in df['Time']]) - df['Time'].min().timestamp()
    df2['Weather_Conditions'] = df['Weather_Conditions']
    return pd.get_dummies(df2)


def filter_location(df: pd.DataFrame = pd.DataFrame()):
    """Returns location columns"""
    if df.empty:
        df = read()
    df = df.dropna()
    df2 = pd.DataFrame()
    df2['Location_Easting_OSGR'] = df['Location_Easting_OSGR']
    df2['Location_Northing_OSGR'] = df['Location_Northing_OSGR']
    return df2


def read():
    with open('./filtered.pkl', 'rb') as file:
        df = pickle.load(file)
    return df


def read_location():
    with open('./locations.pkl', 'rb') as file:
        df = pickle.load(file)
    return df


def read_csv(filename='result.zip'):
    """Reads the file received in the parameter. File must be a zip."""
    print('Reading data...')
    df = pd.read_csv(filename, compression='zip', low_memory=False)
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')
    return df
