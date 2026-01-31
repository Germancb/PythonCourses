import pandas as pd
calories=[420, 380, 390]
indice=["day1", "day2", "day3"]
myvar=pd.Series(calories, indice)   # index= ["day1", "day2", "day3"])
print(myvar)
print(type(myvar))
print(myvar.size)
print(myvar.index)

for ele in myvar.values:
    print(ele)

for ele in myvar.index:
    print(ele)

for ele in myvar:
    print(ele)
print(" ")    
print(myvar["day1"])
print(myvar[["day1", "day3"]])

myvar.astype("i2")
print(myvar.value_counts())
print(" ")   
print(myvar.sort_values())   # no modifica la info si se ve ordenada

# print(myvar.sort_values(inplace = True)) si modfica
# mayvar.sort_index()  es posible

print(myvar +1)   # Operaciones aritméticas 421, 381, 391   No modifica  Hereda de numpy
print(myvar)
# es posible myvar * 2   myvar / 3
print(myvar + myvar)

print(myvar.max(), myvar.argmax(), myvar.min(), myvar.argmin(), myvar.sum())
print(myvar.mode(), myvar.mean(), myvar.median(), myvar.std(), myvar.var(), myvar.count())
print(myvar.describe())
print(myvar.quantile(0.25))
myvar.plot()