# Series-Object:-
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
data=[1,2,3,4,np.nan]
series_1=pd.Series(data)
sports_1=pd.Series([1,2,3,4],index=["Football","Cricket","Basketball","Golf"])
sports_2=pd.Series([2,1,3,4],index=["Football","Cricket","Baseball","Golf"])
print(series_1)
print(type(series_1))
print(sports_1)
print(sports_2)
print(sports_1+sports_2)
#Data Frames:-
np.random.seed(100)
df=pd.DataFrame(np.random.rand(5,5),index="1 2 3 4 5".split(),columns="C1 C2 C3 C4 C5".split())
print(df)
print(df.describe())
print(df.dtypes)
print(df.head(2))
print(df.tail(2))
print(type(df))
print(df.index)
print(df.T)
print(df.sort_index)
df.loc["1","C1"]=881
print(df)
df.loc[1,"C1"]=900
print(df)
print(df.drop(1,axis=0))
print(df.loc[["1","2"],["C2","C3"]])
print(df.iloc[1,4])
print(df.iloc[0,0])
print(df.drop([1]))
print(df.reset_index(drop=True))
print(df.dropna())
print(df.shape) 
#Data Frames with excel:-
dict={
    "names":["Sampath","shikar","warner"],
    "marks":[90,92,100],
    "age":[19,34,33]
}
dfp=DataFrame(dict)
print(df)
dfp.to_csv("panda.csv")
dfp.to_html("panda.html")

