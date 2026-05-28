import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv("creditcard.csv")


print(data.head()) # First 5 rows

print(data.info())

print(data['Class'].value_counts())

legit = data[data.Class == 0]
fraud = data[data.Class == 1]

print("Legitimate Transactions:", legit.shape)
print("Fraud Transactions:", fraud.shape)

print(legit.Amount.describe())
print(fraud.Amount.describe())

legit_sample = legit.sample(n=492)

new_data = pd.concat([legit_sample, fraud], axis=0)

print(new_data['Class'].value_counts())

X = new_data.drop(columns='Class') #splitting features
Y = new_data['Class']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

model = LogisticRegression()

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print("Training Accuracy:", training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print("Test Accuracy:", test_data_accuracy)

print(confusion_matrix(Y_test, X_test_prediction))
print(classification_report(Y_test, X_test_prediction))
input_data = X_test.iloc[0]

prediction = model.predict([input_data])

if prediction[0] == 0:
    print("Legitimate Transaction")
else:
    print("Fraudulent Transaction")
