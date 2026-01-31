import pandas as pd
# DataFrame
mydataset={
    'cars':['BMW','Volvo', 'Ford'],
    'passings':[3,7,2]
}
print(mydataset)
myvar=pd.DataFrame(mydataset)   #DataFrame
print(myvar)
print(type(myvar))