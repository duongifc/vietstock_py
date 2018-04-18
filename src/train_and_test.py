# Test T+3 strategy: supervised (classification) problem: label = 1 if T+3 price > T + 0 price, = 0 otherwise
# Variables: TA indicators + fundamental factors from vietstock

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---------------------------------------------- DATA PREPARATION
diff = 3
target = (price > price.shift(diff)).astype(int)
remove_rows = range(diff)
target.drop(remove_rows, inplace = True)
data.drop(remove_rows, inplace=True)

#----------------------------------------------TRAINING AND TESTING
from sklearn.preprocessing import StandardScaler
from sklearn.utils import resample # if the data is imbalanced
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.neural_network import MLPClassifier

def scores(models, X, y):
    for model in models:
        y_pred = model.predict(X)
        acc = accuracy_score(y, y_pred)
        f1 = f1_score(y, y_pred)
        auc = roc_auc_score(y, y_pred)
        print(model.__class__.__name__)
        print("Accuracy Score: {0:0.2f} %".format(acc * 100))
        print("F1 Score: {0:0.4f}".format(f1))
        print("Area Under ROC Curve Score: {0:0.4f}".format(auc))
        print("\n")
        
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.25, shuffle=False)

models = [
    SVC(),
    RandomForestClassifier(),
    BaggingClassifier(),
    AdaBoostClassifier(),
    ExtraTreesClassifier()
]

for model in models:
    model.fit(X_train, y_train)
scores(models, X_test, y_test)
