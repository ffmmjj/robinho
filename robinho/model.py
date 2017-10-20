import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
import pickle
from robinho.data import load_data


def classifier():
    return Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('sampling', RandomUnderSampler()),
        ('clf', MultinomialNB()),
    ])


def train():
    X, y = load_data()

    print("Fitting data...")
    clf = classifier()
    clf = clf.fit(X, y)

    print("Saving model...")
    pickle.dump(clf, open('model.pkl', 'wb'))


def load_model():
    print("Loading model...")
    return pickle.load(open('model.pkl', 'rb'))


def predict(titles):
    return load_model().predict(titles)
