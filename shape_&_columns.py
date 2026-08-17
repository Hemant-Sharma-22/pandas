import pandas as pd

data = {
    "name": ['mohan','Hemant','Divyam','ritesh'],
    "age" : [20,21,22,23],
    "city": ["mathura", "mumbai", "pune", "lucknow"],
    "salary" : [40000,40000,40000,40000]
}

df= pd.DataFrame(data)
print(df)

print("shape and columns of data set")

print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')

print("-------- head and tail --------")
print(df.head(2))
print(df.tail(2))