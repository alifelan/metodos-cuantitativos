from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from joblib import dump, load
from data import read_location
import pickle
import numpy as np


def train(df):
    scaler = preprocessing.StandardScaler()
    kmeans = KMeans(n_clusters=50)
    pipeline = Pipeline([('Scaler', scaler), ('KMeans', kmeans)])
    # Skip location columns
    pipeline.fit(df.iloc[:, 2:])
    dump(pipeline, 'pipeline.joblib')


def trainRandomForest(df):
    labels = np.array(df['Longitude'], df['Latitude'])
    features = df.drop('Longitude', axis=1)
    features = df.drop('Latitude', axis=1)
    feature_list = list(features.columns)
    features = np.array(features)
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.25, random_state=42)
    scaler = preprocessing.StandardScaler()
    rf = RandomForestRegressor(n_estimators=1000, random_state=42)
    #pipeline = Pipeline([('Scaler', scaler), ('RandomForestRegressor', rf)])
    # Skip location columns
    rf.fit(train_features, train_labels)
    #dump(pipeline, 'pipelineRF.joblib')


def predict(data):
    """Parameters:
    Month: 1-12
    Day: 1-31
    Day_of_Week: 1-7
    Time: in seconds
    Weather_Conditions_Fine with high winds: 0-1
    Weather_Conditions_Fine without high winds
    Weather_Conditions_Fog or mist: 0-1
    Weather_Conditions_Other: 0-1
    Weather_Conditions_Raining with high winds: 0-1
    Weather_Conditions_Raining without high winds: 0-1
    Weather_Conditions_Snowing with high winds: 0-1
    Weather_Conditions_Snowing without high winds: 0-1
    Weather_Conditions_Unknown: 0-1
    """
    print('Loading model...')
    pipeline = load('pipeline.joblib')
    print('Predicting...')
    cluster = pipeline.predict([data])[0]
    df = read_location()
    labels = pipeline.named_steps['KMeans'].labels_
    return df[labels == cluster]
