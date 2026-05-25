# handling missing values:
# import pandas as pd
# data={
#     "Name": ["Sarthak", "Samarth", "Harshit","Tanishk","Abheer"],
#     "Age":[20,21,22,20,None],
#     "Salary":[50000,60000,65000,None, None]
# }
# df=pd.DataFrame(data)
# print("Original Dataframe")
# print(df)
# print(df.isnull().sum())
# df_drop=df.dropna()
# print(df_drop)
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# df['Salary'].fillna(df['Age'].mean(),inplace=True)
# print(df)
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# df['Salary'].fillna(df['Salary'].mean(),inplace=True)
# print(df) 
# print(df.isnull().mean()*100)
# df['Age'].fillna(df['Age'].mean(), inplace=True)
# import pandas as pd
# data= {"Name":["Sarthak", "Tanishk", "Harshit","Vishu","Aishwarya"],
#        "Age":[20,21,19,None,20],
#        "Salary":[50000,55000,60000,None,None]}
# df=pd.DataFrame(data)
# print("Original Dataframe")
# print(df)
# print(df.isnull().sum())
# df_drop=df.dropna()
# print(df_drop)
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# df['Salary'].fillna(df['Salary'].mean(),inplace=True)
# print(df)
# print(df_drop)
# # df['Age'].fillna(df['Age'].mean(),inplace=True)
# # df['Salary'].fillna(df['Salary'].mean(),inplace=True)
# df-drop=df.dropna()
# print(df_drop)

# demo

# from sklearn.linear_model import LinearRegression
# import numpy as np

# # training 
# X = np.array([[1], [2], [3], [4]])
# y = np.array([2, 4, 6, 8])

# # creating
# model = LinearRegression()

# # training
# model.fit(X, y)

# # prediction
# pred = model.predict([[5]])

# print("Prediction:", pred)

# from sklearn.preprocessing import LabelEncoder # scikit-learn library me se labelEncoder tool chahiye jo ki 
# #preprocessing section se le rahe hai (preprocessing section me tools mil jaate hai), Labelencoder convers words to numbers
# import pandas as pd # pandas import

# df=pd.read_csv("sample_data.csv")
# df.columns = df.columns.str.strip()    # removes extra spaces in column names
# df_label=df.copy() # creating duplicate data from original data
# le= LabelEncoder() # creating object
# df_label['Gender_Encoded'] = le.fit_transform(df_label['Gender']) #fit meaans learn from values and transform
# #means convert to numbers after learning, means male=1 and female=0
# df_label['Passed_Encoded']=le.fit_transform(df_label['Passed'])
# print('\nLabel Encoded Data')
# print(df_label[['Name', 'Gender', 'Gender_Encoded', 'Passed', 'Passed_Encoded']].head())


# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# df=pd.read_csv("sample_data.csv")
# df.columns = df.columns.str.strip()
# df_label=df.copy()
# le=LabelEncoder()

# df_label['Gender_Encoded']=le.fit_transform(df_label['Gender'])
# df_label['Passed_Encoded']=le.fit_transform(df_label['Passed'])

# print('\nLabel Encoded Data')
# print(df_label[['Name', 'Gender', 'Gender_Encoded', 'Passed', 'Passed_Encoded']].head())
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# df=pd.read_csv("sample_data.csv")
# df.columns = df.columns.str.strip()
# le=LabelEncoder()
# df_label=df.copy()
# df_label['Gender_Encoded']=le.fit_transform(df_label['Gender'])
# df_label['Passed_Encoded']=le.fit_transform(df_label['Passed'])

# print('\nData')
# print(df_label[['Name', 'Gender', 'Gender_Encoded', 'Passed', 'Passed_Encoded']].head())
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# df= pd.read_csv("sample_data.csv")
# df.columns = df.columns.str.strip()

# le=LabelEncoder()
# df_2=df.copy()
# df_2['Gender_Encoded']=le.fit_transform(df_2['Gender'])
# df_2['Passed_Encoded']=le.fit_transform(df_2['Passed'])

# print("Data")
# print(df_2[['Name', 'Gender','Gender_Encoded', 'Passed', 'Passed_Encoded']].head())
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# df=pd.read_csv("sample_data.csv")

# le=LabelEncoder()
# df_2=df.copy()
# df_2['Gender_Encoded']=le.fit_transform(df_2['Gender'])
# df_2['Passed_Encoded']=le.fit_transform(df_2['Passed'])
# print("Data")
# print(df_2[['Name','Gender', 'Gender_Encoded','Passed','Passed_Encoded']])

# df_encoded=pd.get_dummies(df_2, columns=['City'])
# print('\n One hot encoded data (City)')
# print(df_encoded)
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# scaler= StandardScaler()
# x_scaled=scaler.fit_transform
# scaler=MinMaxScaler()
# x_scaled=scaler.fit_transform()


# import pandas as pd
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# from sklearn.model_selection import train_test_split
# data={
#     'StudyHours':[1,2,3,4,5],
#     'TestScore':[40,50,60,70,80]
# }
# df=pd.DataFrame(data)
# # standard scaler
# standard_scaler=StandardScaler()
# standard_scaled=standard_scaler.fit_transform(df)

# print("standard scaler output")
# print(pd.DataFrame(standard_scaled, columns=['StudyHours', 'TestScore']))

# feature scaling
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# import pandas as pd

# scaler=StandardScaler()
# x_scaled=scaler.fit_transform()

# scaler=MinMaxScaler()
# x_scaled=scaler.fit_transform()
 
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# scaler=StandardScaler()
# X_scaled=scaler.fit_transform()

# scaler=MinMaxScaler()
# X_scaled=scaler.fit_transform()


# import pandas as pd
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# from sklearn.model_selection import train_test_split

# data={'Studyhours':[1,2,3,4,5],
#       'TestScore':[40,50,60,70,80]}

# df=pd.DataFrame(data)
# # standard scaler
# Standard_Scaler=StandardScaler()

# Standard_Scaled=StandardScaler.fit_transform(df)
# print("Standard Scaler Output")
# print(pd.DataFrame(Standard_Scaled, columns=['StudyHours', 'TestScore']))

# min_max_Scaler=MinMaxScaler()
# min_max_Scaled=MinMaxScaler.fit_transform(df)
# print("Min max scaler output")
# print(pd.DataFrame(min_max_Scaler, columns=["StudyHours", "TestScore"]))
# X=df[['StudyHours']]
# y=df[['TestScore']]
# X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=42)
# print("Training data")
# print(X_train)
# print("Testing data")
# print(X_test)
# label encoding
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# df=pd.read_csv("sample_data.csv")
# df_2=df.copy()
# le=LabelEncoder()
# df_2['Gender_Encoded']=le.fit_transform(df_2['Gender'])
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd
# df=pd.read_csv("sample_data.csv")
# df_2=df.copy()
# le=LabelEncoder()
# df_2['Gender_Encoded']=le.fit_transform(df_2['Gender'])
# # one hot encoding
# # from sklearn.preprocessing import 
# df_3=pd.get_dummies(df_2, columns=['City'])
# print(df_3)
# feature scaling
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# scaler=StandardScaler()
# X_scaled=scaler.fit_transform()

# scaler-MinMaxScaler()
# X_scaled=scaler.fit_transform()
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# import pandas as pd
# from sklearn.model_selection import train_test_split
# data={
#     'StudyHours':[1,2,3,4,5],
#     'TestScore':[40,50,60,70,80]
# }
# df=pd.DataFrame(data)
# standard_scaler=StandardScaler()
# Standard_Scaled=StandardScaler.fit_transform(df)
# print(pd.DataFrame(Standard_Scaled, columns=['StudyHours', 'TestScore']))
# min_max_scaler=MinMaxScaler()
# min_max_scaled=MinMaxScaler.fit_transform(df)
# print(pd.DataFrame(min_max_scaled, columns=['StudyHours', 'TestScore']))
# standard scaler and minmax sclaer
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# standard_scaler=StandardScaler()
# standard_scaled=StandardScaler.fit_transform()

# Min_Max_Scaler=MinMaxScaler()
# Min_Max_Scaled=MinMaxScaler.fit_transform()
# import pandas as pd
# from sklearn.preprocessing import StandardScaler, MinMaxScaler      
# from sklearn.model_selection import train_test_split
# data={
#     'TestScore':[30,40,50,60,70],
#     'StudyHours':[2,3,4,5,6]
# }
# df=pd.DataFrame(data)
# scaler = StandardScaler()
# Standard_Scaled = scaler.fit_transform(df)

# print(pd.DataFrame(Standard_Scaled, columns=['TestScore','StudyHours']))
# from sklearn.linear_model import LinearRegression
# X= [[1],[2],[3],[4],[5]]
# y=[40,50,60,70,80]
# model = LinearRegression()
# model.fit(X, y)
# hours= int(input("Enter the number of hoiurs you have studied"))
# predicted_marks=model.predict([[hours]])
# print(f"predicted marks are {predicted_marks}")
# from sklearn.linear_model import LinearRegression
# X= [[1],[2],[3],[4],[5]]
# y=[40,50,60,65,70]
# model = LinearRegression() #object creation
# model.fit(X,y)
# hours = int(input("enter how many hours you studied = "))
# predicted_marks=model.predict([[marks]]) # value is passed in a 2d list
# print(f"your marks are {predicted_marks}")
# from sklearn.linear_model import LinearRegression
# X=[[3],[4],[5],[6],[7]]
# y=[40,50,65,75,80]
# model=LinearRegression()
# model.fit(X,y)
# hours=int(input("Enter the number of hours"))
# predicted_marks=model.predict([[hours]])
# print(f"the marks as per your hours are {predicted_marks}")
# logistic regression
# from sklearn.linear_model import LogisticRegression
# X=[[1],[2],[3],[4],[5]] #hours studied
# y=[0,0,0,1,1] #pass or fail
# model=LogisticRegression()
# model.fit(X,y)
# hours=int(input("Enter the number of hours"))
# final_result=model.predict([[hours]])

# # print(f"The final result is{final_result}")
# if final_result == 1:
#     print("passed")
# else:
#     print("failed")
# from sklearn.linear_model import LogisticRegression
# X=[[1],[2],[3],[4],[5]]
# y=[0,0,0,1,1]
# model=LogisticRegression()
# model.fit(X,y)
# hours=float(input("Enter the number of hours you studied"))
# result=model.predict([[hours]])
# print(f"The result as per the hours studied is {result}")
# if result==1:
#     print("pass")
# else:
#     print("fail")
# K NEAREST NEIGHBOURS CLASSIFICATION
# from sklearn.neighbors import KNeighborsClassifier
# X=[
#     [180,7],
#     [200,7.5],
#     [250,8],
#     [300,8.5],
#     [350,9],
#     [360,9.5]
# ]
# y=[0,0,0,1,1,1]
# model=KNeighborsClassifier(n_neighbors=3)
# model.fit(X,y)

# weight=float(input("Enter the weight"))
# size=float(input("enter the size"))

# pred=model.predict([[weight,size]])[0]
# print(f"the fruit is {pred}")
# if pred==0:
#     print("Apple")
# else:
#     print("Orange")
# from sklearn.neighbors import KNeighborsClassifier
# X=[
#     [180,7],
#     [200,7.5],
#     [250,8],
#     [300,8.5],
#     [350,9],
#     [360,9.5]
# ]
# y=[0,0,0,1,1,1]
# model=KNeighborsClassifier(n_neighbors=3)
# model.fit(X,y)

# weight=float(input("Enter the weight"))
# size=float(input("Enter the size"))
# pred=model.predict([[weight,size]])[0]

# print(f"THe fruit as per given weight and size is {pred}")
# if pred==0:
#     print("Apple")
# else:
#     print("Orange")
# from sklearn.tree import DecisionTreeClassifier

# X=[
# [7,2], #A
# [8,3], #A
# [9,8], #O
# [10,9] #O
# ]

# y=[0,0,1,1]

# model=DecisionTreeClassifier()

# model.fit(X,y)
# size=int(input("Enter the size"))
# colour=int(input("Enter the colour grade"))

# pred=model.predict([[size,colour]])[0]

# if pred==0:
#     print("fruit is apple")
# else:
#     print("fruit is orange")

# from sklearn.tree import DecisionTreeClassifier
# X=[
#     [7,2],
#     [8.3],
#     [9,8],
#     [10,9]
# ]
# y=[0,0,1,1]

# model.fit(X,y)
# size=int(input("Enter the size"))
# colour=int(input("Enter the colour grade"))
# pred=model.predict([[size,colour]])[0]
# if pred==0:
#     print("Apple")
# else:
#     print("Orange")

# model evaluation  evaluation metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true=[1,0,1,1,0,1,0] #what actually happened
y_pred= [1,0,1,0,0,1,1] #what model predicted

print("accuracy:", accuracy_score(y_true, y_pred))
print("precision:", precision_score(y_true, y_pred))
print("recall:", recall_score(y_true, y_pred))
print("f1 score", f1_score(y_true, y_pred))

print(accuracy_score(y_true, y_pred)*100)
  