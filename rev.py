# import numpy
# import pandas as pd
# data={
#     "name":["a","b","c","d"],
#     "age":[20,21,22,None],
#     "salary":[10000,20000,None,35000]
# }
# df=pd.DataFrame(data)
# df_2=df.dropna()

# print(df_2)
# df['age']=df['age'].fillna(df['age'].mean())
# df['salary']=df['salary'].fillna(df['salary'].mean())
# print(df)
# Encoding:
# label encoding
# from sklearn.preprocessing import LabelEncoder
# import numpy as np
# import pandas as pd
# df=pd.read_csv("sample_data.csv")

# df_label=df.copy()
# le= LabelEncoder()
# df_label['Gender_Encoded']=le.fit_transform(df_label['Gender'])
# print(df_label)
# from sklearn.preprocessing import LabelEncoder
# import numpy as np
# import pandas as pd
# df=pd.read_csv("sample_data.csv")
# df_2=df.copy()

# le=LabelEncoder()
# df_2['Gender_Encoded']=le.fit_transform(df_2['Gender'])
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# df=pd.read_csv("Sample_data.csv")
# df_2=df.copy()

# le=LabelEncoder()
# df_2['Gender_Encoded']=le.fit_transform(df_2['Gender'])
# print(df_2)

# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# df=pd.read_csv("sample_data.csv")
# df_2=df.copy()

# le=LabelEncoder()
# df_2['Gender_Encoded']=le.fit_transform(df_2['Gender'])

# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data=pd.read_csv("sample_data.csv")
# data_2=data.copy()
# le=LabelEncoder()

# data_2['Gender_Encoded']=le.fit_transform(data_2['Gender'])
# print(data_2)

# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data=pd.read_csv('sample_data.csv')
# data_2=data.copy()

# le=LabelEncoder()

# data_2['Gender_Encoded']=le.fit_transform(data_2['Gender'])
# print(data_2)

# one hot encoding
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data=pd.read_csv('sample_data.csv')
# data_2=data.copy()

# le=LabelEncoder()

# data_2['Gender_Encoded']=le.fit_transform(data_2['Gender'])
# print(data_2)

# data_encoded=pd.get_dummies(data_2, columns=['City'], dtype=int)
# print(data_encoded)
# from sklearn.preprocessing import LabelEncoder
# import numpy as np
# import pandas as pd

# data=pd.read_csv('sample_data.csv')
# data_2=data.copy()

# le=LabelEncoder()
# data_2['Gender_Encoded']=le.fit_transform(data_2['Gender'])

# data_encoded=pd.get_dummies(data_2, columns=['City'], dtype=int)
# print(data_encoded)

# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# data=pd.read_csv('Sample_data.csv')
# data_2=data.copy()

# le=LabelEncoder()

# data_2['Gender_Encoded']=le.fit_transform(data_2['Gender'])

# data_encoded=pd.get_dummies(data_2, columns=['City'],dtype=int)
# print(data_encoded)

# Feature scaling
# used to normalize or standardize the values
# minmax scaler scales the valuesb/w 0 and 1
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# scaler= StandardScaler()
# X_scaled=scaler.fit_transform()
# scaler=MinMaxScaler()
# X_scaled=scaler.fit_transform()


from sklearn.preprocessing import StandardScaler, MinMaxScaler

from sklearn.model_selection import train_test_split
import pandas as pd

data={
    "Studyhours":[1,2,3,4,5],
    "Testscore":[40,50,55,65,80]
}
df=pd.DataFrame(data)
print(df)
Standard_scaler=StandardScaler()