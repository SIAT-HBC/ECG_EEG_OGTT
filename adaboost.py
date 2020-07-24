//start here

from sklearn.datasets import make_classification
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
  
ECGEEG = pd.read_csv("C:/Dataset/participant_ECG_EEG.csv") 

X_train, X_test, y_train, y_test = train_test_split(dataX, datay, test_size = 0.20)

model = AdaBoostClassifier()
# fit the model on the whole dataset
model.fit(X_train, y_train)
 
pred_test = model.predict(X_test)
print(confusion_matrix(y_test,pred_test))
print(classification_report(y_test,pred_test))
//end here