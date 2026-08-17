import pandas as pd

data = {
    "name": ['mohan','Hemant','Divyam','ritesh'],
    "age" : [20,21,22,23],
    "city": ["mathura", "mumbai", "pune", "lucknow"],
    "salary" : [40000,40000,40000,40000]
}

df= pd.DataFrame(data)
print(df)

print("description of data set")
print(df.describe())