import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

ECGEEG = pd.read_csv("C:/Dataset/participant_ECG_EEG.csv")
 
ECGEEG.shape 

ECGEEG.head()

dataX = ECGEEG.drop('Class', axis=1)
datay = ECGEEG['Class']

X_train, X_test, y_train, y_test = train_test_split(dataX, datay, test_size = 0.20)

ECGEEGclassifier = SVC(kernel='linear')
ECGEEGclassifier.fit(X_train, y_train)

y_predicted = ECGEEGclassifier.predict(X_test)


print(confusion_matrix(y_test,y_predicted))
print(classification_report(y_test,y_predicted))
 