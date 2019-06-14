import pandas as pd
from sklearn import preprocessing


def filter(df: pd.DataFrame = pd.DataFrame()):
    """Returns only important columns"""
    if df.empty:
        df = read()
    df2 = pd.DataFrame()
    df2['Location_Easting_OSGR'] = df['Location_Easting_OSGR']
    df2['Location_Northing_OSGR'] = df['Location_Northing_OSGR']
    df2['Date'] = df['Date']
    df2['Day_of_Week'] = df['Day_of_Week']
    df2['Date'] = df['Date']
    df2['Speed_limit'] = df['Speed_limit']
    df2['Light_Conditions'] = df['Light_Conditions']
    df2['1st_Road_Class'] = df['1st_Road_Class']
    df2['2nd_Road_Class'] = df['2nd_Road_Class']
    df2['1st_Road_Number'] = df['1st_Road_Number']
    df2['2nd_Road_Number'] = df['2nd_Road_Number']
    df2['Weather_Conditions'] = df['Weather_Conditions']
    df2['Urban_or_Rural_Area'] = df['Urban_or_Rural_Area']
    df2['Year'] = df['Year']
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
