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
    features = df.drop('Longitude', axis = 1)
    features = df.drop('Latitude', axis = 1)
    feature_list = list(features.columns)
    features = np.array(features)
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
    scaler = preprocessing.StandardScaler()
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    #pipeline = Pipeline([('Scaler', scaler), ('RandomForestRegressor', rf)])
    # Skip location columns
    rf.fit(train_features, train_labels);
    #dump(pipeline, 'pipelineRF.joblib')

def predict(data):
    print('Loading model...')
    pipeline = load('pipeline.joblib')
    print('Predicting...')
    cluster = pipeline.predict([data])[0]
    df = read_location()
    labels = pipeline.named_steps['KMeans'].labels_
    return df[labels == cluster]
