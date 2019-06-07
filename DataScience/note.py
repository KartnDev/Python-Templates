import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
digits = pd.read_csv('Samples/train.csv', header = None)
dataset = pd.read_csv('Samples/test.csv', header = None, dtype=int)

tree = RandomForestClassifier(n_estimators=1000)

train = digits.values()

X = train[:,1:-1]
y = train[:, 0]

tree.fit(X, y)

dataset_matrix = dataset.as_matrix()

Xtest = dataset_matrix[:, 1:-1]
ytest = dataset_matrix[:, 0]

ypred = tree.predict(Xtest)
print(classification_report(ypred, ytest))