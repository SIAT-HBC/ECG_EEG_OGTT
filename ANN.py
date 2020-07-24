
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import classification_report, confusion_matrix

model = Sequential()
model.add(Dense(10, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

ECGEEG = pd.read_csv("C:/Dataset/participant_ECG_EEG.csv")
ECGEEG = StandardScaler().fit_transform(ECGEEG)
dataX = ECGEEG.drop('Class', axis=1)
datay = ECGEEG['Class']

X_train, X_test, y_train, y_test = train_test_split(dataX, datay, test_size = 0.20)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=100, batch_size=10)

predictions = model.predict_classes(X_test)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))