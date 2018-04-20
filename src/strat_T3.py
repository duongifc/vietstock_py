# Test T+3 strategy: supervised (classification) problem: label = 1 if T+3 price > T + 0 price, = 0 otherwise
# Variables: TA indicators + fundamental factors from vietstock

import numpy as np
import pandas as pd

#---------------------------------------------- DATA PREPARATION
col_names = ["Date", "KLNY","KLCPDLH","GTC","T","S","TKLGD","TGTGD","VHTT","CN",\
             "TN","GYG","GD1","KLD1","GTD1","GD2","KLD2","GTD2","GD3","KLD3","GTD3",\
             "TGG","TGPTG","GDC","KLDC", "BQM","BQB","DM","DB","LDM","LDB","LDMB", \
             "KLDM","KLDB","KLDMB","KLGDKL","GTGDKL","KLGDTT","GTGDTT"]

data = pd.read_csv("Hose_ANV_02_26_16_03_26_18.csv", names= col_names, skiprows= 1)

# Rename and reformat to standard convention
data["Date"] = pd.to_datetime(data["Date"])
from_name = ["GTC","CN","TN","GD3","TKLGD"]
to_name = ["Open","High","Low","Close","Volume"]
for f_name, t_name in zip(from_name,to_name):
    data.rename(columns={f_name: t_name}, inplace=True)

# drop redundant variables and create output variable
price = data['Close']
drop_col = ["Date","KLNY","KLCPDLH","Open","T","S","Volume","TGTGD","High","Low","GYG","GD2","Close",\
            "TGG","GDC","KLDC","LDMB","KLDM","KLDB","KLDMB","KLGDKL"]
data.drop(drop_col, axis = 1, inplace=True)

# train/test split
test_prop = 0.2
length = np.shape(data)[0]
test_input = data[int(length*test_prop):]
data = data[:int(length*test_prop)]
test_output = price[int(length*test_prop):]
price = price[:int(length*test_prop)]

# Formulate T3 strategy
target = (price > price.shift(3)).astype(int)
target = target[3:]
data = data[:-3]

target_test = (test_output > test_output.shift(3)).astype(int)
target_test = target_test[3:]
test_input = test_input[:-3]

#----------------------------------------------TRAINING AND TUNING
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier,\
                            AdaBoostClassifier, ExtraTreesClassifier
from sklearn.neural_network import MLPClassifier

def scores(models, X, y):
    for model in models:
        y_pred = model.predict(X)
        acc = accuracy_score(y, y_pred)
        f1 = f1_score(y, y_pred)
        auc = roc_auc_score(y, y_pred)
        print(model.__class__.__name__)
        print("Accuracy Score: {0:0.2f} %".format(acc * 100))
        print("F1 Score: {0:0.3f}".format(f1))
        print("Area Under ROC Curve Score: {0:0.3f}".format(auc))
        print("\n")
        
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2)
m = np.mean(X_train)
sd = np.std(X_train)
X_train = (X_train - m)/sd
X_test = (X_test - m)/sd

# loop search for tuning parameters
ensemble = [RandomForestClassifier(n_estimators=20),
            BaggingClassifier(n_estimators=20),
            ExtraTreesClassifier(n_estimators=20)
           ]

my_tab = []
for model in ensemble:
    f1s = []
    for i in range(120):
        model.random_state_ = i
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        f1 = f1_score(y_test, y_pred)
        f1s.append(f1)
    my_dict = {
        'Clf': model.__class__.__name__,
        'Ran_state': [i for i, j in enumerate(f1s) if j == max(f1s)],
        'F1_score': max(f1s)
    }
    my_tab.append(my_dict)

# Use optimal tuning parameters for the models
models = [
    SVC(C = 1.01,kernel='rbf'),
    RandomForestClassifier(n_estimators=20, random_state=1),
    BaggingClassifier(n_estimators=20, random_state=117), # loop search
    ExtraTreesClassifier(n_estimators=20, bootstrap=True, random_state=22),
    AdaBoostClassifier(random_state=123)
]

for model in models:
    model.fit(X_train, y_train)
    
scores(models, X_test, y_test)

#----------------------------------------------TESTING
test_input = (test_input - m)/sd

bagging = BaggingClassifier(n_estimators=20, random_state=101)
bagging.fit(X_train, y_train)
y_pred = bagging.predict(test_input)
f1_score(target_test, y_pred)

#----------------------------------------------COMMENT
# This naive model doesnt work well.
