# Estimated values inplace of missing values
        # preserve data integrity
        # smooth trend
        # avoid droping rows
        # Good with Time-Series data

# syntax:- 
#         df.interpolate(method="linear", axis=0/1, inplace= True)  

# there are multiple methods :-> linear, polynomial, time


import pandas as pd

data= {
    "name": ["ram","shyam","ghanshyam","murali","pritam"],
    "age":[10, None, None, 40,50]
}

df= pd.DataFrame(data)
print(df)

print("using interpolation")
df["age"]= df["age"].interpolate(method="linear")
print(df)