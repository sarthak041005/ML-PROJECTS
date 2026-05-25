# # Import libraries
# import pandas as pd
# import numpy as np

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# # Load dataset
# data = pd.read_csv("creditcard.csv")

# # Show first 5 rows
# print(data.head())

# # Dataset information
# print(data.info())

# # Check class distribution
# print(data['Class'].value_counts())

# # Separate genuine and fraud transactions
# legit = data[data.Class == 0]
# fraud = data[data.Class == 1]

# print("Legitimate Transactions:", legit.shape)
# print("Fraud Transactions:", fraud.shape)

# # Compare amount statistics
# print(legit.Amount.describe())
# print(fraud.Amount.describe())

# # Undersampling
# legit_sample = legit.sample(n=492)

# new_data = pd.concat([legit_sample, fraud], axis=0)

# print(new_data['Class'].value_counts())

# # Split features and target
# X = new_data.drop(columns='Class')
# Y = new_data['Class']

# # Train test split
# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, test_size=0.2, stratify=Y, random_state=2
# )

# # Model training
# model = LogisticRegression()

# model.fit(X_train, Y_train)

# # Accuracy on training data
# X_train_prediction = model.predict(X_train)
# training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# print("Training Accuracy:", training_data_accuracy)

# # Accuracy on test data
# X_test_prediction = model.predict(X_test)
# test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# print("Test Accuracy:", test_data_accuracy)

# # Confusion matrix
# print(confusion_matrix(Y_test, X_test_prediction))

# # Classification report
# print(classification_report(Y_test, X_test_prediction))

# # Predict on new data
# input_data = X_test.iloc[0]

# prediction = model.predict([input_data])

# if prediction[0] == 0:
#     print("Legitimate Transaction")
# else:
#     print("Fraudulent Transaction")