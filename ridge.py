
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

ECGEEG = pd.read_csv("C:/Dataset/participant_ECG_EEG.csv") 

#define train and testing dataset
X_train, X_test, y_train, y_test = train_test_split(dataX, datay, test_size = 0.20)

steps = [('scaler', StandardScaler()),
         ('ridge', Ridge())]


pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'ridge__alpha':np.logspace(-4, 0, 50)}


eecg = GridSearchCV(pipeline, parameters, cv=3)

eecg.fit(X_train, y_train)

pred_train=eecg.predict(X_train)

pred_test=eecg.predict(X_test)

print(confusion_matrix(y_test,pred_test))
print(classification_report(y_test,pred_test))
