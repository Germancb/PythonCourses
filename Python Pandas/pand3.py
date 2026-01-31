import pandas as pd
data={
"calories":[420, 380, 395],
"duration":[50,40,45]
}
indice=["Day1", "Day2", "Day3"]
myvar=pd.DataFrame(data)
print(myvar)
print(type(myvar))
print(myvar.loc[[0,1]])

df=pd.DataFrame(data, indice)   # index=["Day1", "Day2", "Day3"])
print(df)
print(df.loc["Day2"])