# import pandas as pd
# data={
#     "Name": ['sarthak', 'aishwarya','rajeev'],
#     "age": [10,20,30],
#     "city":['mbd', "mum", "del"]
# }
# df=pd.DataFrame(data)
# print(df)
# import pandas as pd
# # df.to_excel("pandas_ch1.xlsx", index=False)
# df= pd.read_csv("sales_data_sample.csv", encoding="latin")
# print("show first 10 rows")
# print(df.head())
# print("show last 10 rows")
# print(df.tail())
# import pandas as pd
# print(pd.__version__)
# # series
# import pandas as pd
# data=[10,20,30]
# series=pd.Series(data, index=["a", "b", "c"])
# print(series)
# import pandas as pd
# data=[10,20,30]
# series = pd.Series(data, index=["a", "b", "c"])
# print(series.loc["c"])
# import pandas as pd
# data = [10,20,30]
# series= pd.Series(data, index=["a", "b", "c"])
# print(series.loc["c"])
# data1=series.loc["b"]
# print(data1)
# print(series.iloc[0])
# import pandas as pd
# data=[10,20,30,40,50]
# series=pd.Series(data, index=["a", "b", "c", "1", "2"])
# print(series[series<=30])
# import pandas as pd
# data= {"name":"sarthak",
#        "age":"21",    
#        "city":"blr"}
# series=pd.Series(data)
# series.loc["age"]+="2"
# print(series.loc["city"])
# print(series.loc["age "])
# import pandas as pd
# data=["bulbasaur", "ivysaur","vanusaur", "charmander", "charmelion", "charizard"]
# series=pd.Series(data, index=["1","2","3","4","5","6"])
# print(series) 
# # dataframe
# import pandas as pd
# data={
#     "Name":["ross","monica","rachel"],
#     "Age":[30,35,50]
# }
# df=pd.DataFrame(data, index=["Employee 1", "Empolyee 2","Empolyee 3"])
# # add new column
# df["job"]=["Manager","N/A","Cashier"]
# # add new row
# new_row=pd.DataFrame([{"Name": "Chandler", "Age":"28", "job":"Transponsterr"}], index=["Employee 4"])
# df=pd.concat([df, new_row])
# print(df)
# import pandas as pd
# data={
#     "name":["a","b","c"],
#     "age":[10,20,30]
# }
# df=pd.DataFrame(data, index=["1","2","3"])
# # print(df)
# df["role"]=["sde1","sde2","sde3"]
# new_row=pd.DataFrame([{"name": "d", "age": "35","role":"sde2"}], index=["4"])
# df=pd.concat([df,new_row])
# print(df)
# df=pd.DataFrame(data, index=["a","b","c"])
# print(df)
# import pandas as pd
# df= pd.read_csv("sales_data_sample.csv", encoding="latin1")
# print(df)
# import pandas as pd
# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
# print(df)
# import pandas as pd
# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
# print(df.columns)
# print(df[["SALES", "COUNTRY", "DEALSIZE"]]) 
# import pandas as pd
# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
# print(df)
# import pandas as pd
# df=pd.read_csv("sales_data_sample.csv", encoding="latin1", index_col="COUNTRY")
# print(df.loc["USA"])
# import pandas as pd
# df=pd.read_csv("sales_data_sample.csv",encoding="latin1", index_col="DEALSIZE")
# print(df.loc["Small",["STATUS", "PRICEEACH"]].to_string())
# import pandas as pd
# df = pd.read_csv(
#     "sales_data_sample.csv",
#     encoding="latin1",
#     index_col="ORDERNUMBER"
# )
# print((df["INDEX"]>=4) &(df["INDEX"]<=10) , ["PRICEEACH", "DEALSIZE"])
    # restart
# filtering data in series
# import pandas as pd
# data=[100.1,102.2,104.3]
# series=pd.Series(data, index=("a","b","c"))
# print(series.loc["a"])
# print(series.iloc[2])
# series.loc["b"]=103.2
# print(series.iloc[1])
# import pandas as pd
# data= [100,102,104,200,202]
# series= pd.Series(data, index=["a","b","c","d","e"])
# print(series)
# print(series[series>=200])
# print(series[series<200])
# filtering data in dictionary
# import pandas as pd
# data={"day 1": 1800,
#       "day 2": 2200,
#       "day 3":2000
#       }
# series= pd.Series(data)
# print(series)
# # series.loc["day 1"]+=250
# print(series[series>=2000])
# print(series.iloc[1])
# import pandas as pd
# data=["bulbasaur", "ivysaur","vanusaur", "charmander", "charmelion", "charizard"]
# series=pd.Series(data, index=["1","2","3","4","5","6"])
# print(series) 
# dictionary
# import pandas as pd
# data= {
#     "NAME":["CHANDLER","MONICA","ROSS"],
#     "AGE":[23,25,31]
# }
# df=pd.DataFrame(data, index=["emp 1","emp 2","emp 3"])
# df["JOB"]=["MANAGER", "COOK","CASHIER"]
# new_row=pd.DataFrame([{"NAME":"SANDY", "AGE":30, "JOB":"ACTOR"}])
# print(df)
# add new row
# import pandas as pd
# data={
#     "name":["a","b","c"],
#     "age":[10,20,30]
# }
# df=pd.DataFrame(data)
# df["JOB"]=["X","Y","Z"]
# df2=pd.DataFrame([{"name":"d","age":40, "JOB":"w"}])
# df=pd.concat([df,df2])
# print(df)
# add new rows
# import pandas as pd
# data={"name":["a","b","c"],
#       "age":[10,20,30]
#       }
# df=pd.DataFrame(data)
# df("job")=["x","y","z"]
# selection by column/s
# import pandas as pd
# df= pd.read_csv("pokemon.csv")
# print(df[["Name", "Height", "Weight"]].to_string())
# selection by row/s
# import pandas as pd
# df= pd.read_csv("pokemon.csv", index_col="Name")
# print(df)
# print(df.loc["Mewtwo"])
# selected data
# import pandas as pd
# df= pd.read_csv("pokemon.csv", index_col="Name")
# print(df.loc["Squirtle":"Golbat",["Weight", "Height"]])
# by indexing
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# print(df.iloc[0:51:3,0:4])
# Find name of pokemon
# import pandas as pd
# df=pd.read_csv("pokemon.csv", index_col="Name")
# Pokemon=input("Enter name of pokemon")
# try:
#     print(df.loc[Pokemon])
# except KeyError:
#     print(Pokemon," not found")
# Filtering data
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# # tall=df[df["Height"]>=3]
# # heavy=df[df["Weight"]>=200]
# legendary= df[df["Legendary"]==True]
# print(legendary)
# # print(heavy)
# # print(tall)
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# water_pokemon=df[df["Type1"]=="Water"]
# print(water_pokemon)
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# flying_pokemon= df[df["Type2"]=="Flying"]
# print(flying_pokemon)
# or case
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# water_pokemon=df[(df["Type1"]=="Water")] | (df["Type2"]=="Water")
# print(water_pokemon)
# import pandas as pd
# df=pd.read_csv("pokemon.csv", index_col="Name")
# pokemon=input("enter name")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print([pokemon], "not found")
# aggregate function for entire dataframe
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# # print(df.mean(numeric_only="True"))
# # print(df.sum(numeric_only="True"))
# # print(df.min(numeric_only="True"))
# # print(df.max(numeric_only="True"))
# print(df.count())
# aggregate functions for a single column
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# print(df["Height"].mean())
# print(df["Weight"].max())
# print(df["Weight"].sum())
# print(df["Weight"].min())
# print(df["Weight"].count())
# print(df["Type2"].count())
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# group= df.groupby("Type1")
# print(group["Height"].mean())
# data cleaning
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df1=df.drop(columns=["Legendary", "No"])
# print(df1)
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df1=df.dropna(subset=["Type2"])
# print(df1.to_string())
# replace such rows
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df1=df.fillna({"Type2":"None"})
# print(df1.to_string)
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# # print(df)
# df1=df.fillna({"Type2": "ATMKBFJGG"})
# print(df1.to_string())
# change instance of an existing value
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df["Type1"]=df["Type1"].replace({"Grass":"GRASS"})
# # print(df.to_string())
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df["Type1"]=df["Type1"].replace({"Grass":"GRASS"})
# print(df.to_string())
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df["Type2"]=df["Type2"].replace({"Poison":"Venom", "Grass":"GRASS"})
# print(df.to_string())
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df["Name"]=df["Name"].str.lower()
# print(df.to_string())
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# import pandas as pd
# df=pd.read_csv("pokemon.csv")
# df["Name"]=df["Name"].str.lower()
# print(df.to_string())
# df=pd.read_csv("pokemon.csv")
# df=df.drop_duplicates()
# print(df.to_string())