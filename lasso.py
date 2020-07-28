from sklearn.datasets import load_diabetes
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LassoCV
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
col_list = ["RR_I","HR","R_H","P_H","QRS","PRQ","QT","QTC","ST"]
glu_list=["glucose"]
ECGdata = pd.read_csv("C:/Dataset/participant_ECG1.csv",usecols=col_list)
ECGglucosedata = pd.read_csv("C:/Dataset/participant_ECG1.csv",usecols=glu_list)

clf = LassoCV().fit(ECGdata, ECGglucosedata)
coeficient1 = np.abs(clf.coef_)

ECGdata = pd.read_csv("C:/Dataset/participant_ECG2.csv",usecols=col_list)
ECGglucosedata = pd.read_csv("C:/Dataset/participant_ECG2.csv",usecols=glu_list)

clf = LassoCV().fit(ECGdata, ECGglucosedata)
coeficient2 = np.abs(clf.coef_)

ECGdata = pd.read_csv("C:/Dataset/participant_ECG3.csv",usecols=col_list)
ECGglucosedata = pd.read_csv("C:/Dataset/participant_ECG3.csv",usecols=glu_list)

clf = LassoCV().fit(ECGdata, ECGglucosedata)
coeficient3 = np.abs(clf.coef_)

print(coeficient1)
print(coeficient2)
print(coeficient3)