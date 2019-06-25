from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from joblib import dump, load
from data import read, filter_location
import pickle


def train(df):
    scaler = preprocessing.StandardScaler()
    kmeans = KMeans(n_clusters=50)
    pipeline = Pipeline([('Scaler', scaler), ('KMeans', kmeans)])
    # Skip location columns
    pipeline.fit(df.iloc[:, 2:])
    dump(pipeline, 'pipeline.joblib')


def predict(data):
    print('Loading model...')
    pipeline = load('pipeline.joblib')
    print('Predicting...')
    cluster = pipeline.predict([data])[0]
    df = read()
    labels = pipeline.named_steps['KMeans'].labels_
    return df[labels == cluster]
