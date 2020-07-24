import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import classification_report, confusion_matrix

ECGEEG = pd.read_csv("C:/Dataset/participant_ECG_EEG.csv")
 
ECGEEG.shape 

ECGEEG.head()
X_train, X_test, y_train, y_test = train_test_split(dataX, datay, test_size = 0.20)

clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test) 
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
