import pandas as pd
data={
"calories":[420, 380, 395],
"duration":[50,40,45]
}
myvar=pd.DataFrame(data)
print(myvar)
print(type(myvar))