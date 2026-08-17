import pandas as pd

data = {
    "name": ['mohan','Hemant','Divyam','ritesh'],
    "age" : [20,21,22,23],
    "city": ["mathura", "mumbai", "pune", "lucknow"]
}

df= pd.DataFrame(data)
df.to_csv("sample.csv", index=False)
print(df)

print("Displaying info() of data set")
print(df.info())