import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler

dfbefore = pd.read_csv('C:/Dataset/participant_ECG_before.csv')
dfpeak = pd.read_csv('C:/Dataset/participant_ECG_peak.csv')
dfend = pd.read_csv('C:/Dataset/participant_ECG_end.csv')


scaled_before = StandardScaler().fit_transform(dfbefore)
scaled_peak = StandardScaler().fit_transform(dfpeak)
scaled_end = StandardScaler().fit_transform(dfpeak)

features_b= scaled_before.T
features_p= scaled_peak.T
features_e= scaled_end.T

cov_matrixb = np.cov(features_b)
cov_matrixp = np.cov(features_p)
cov_matrixe = np.cov(features_e)

val_b, vect_b = np.linalg.eig(cov_matrixb)
val_p, vect_p = np.linalg.eig(cov_matrixp)
val_e, vect_e = np.linalg.eig(cov_matrixe)

print(val_b)
print(val_p)
print(val_e)
