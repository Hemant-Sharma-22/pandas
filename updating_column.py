import pandas as pd

data= {
    "name": ["ram", "shyam","gopinath", "ghanshyam","Mohan","krishna","pritam", "pyare","devkinandan","baanke","madav","gopal"],
    "age":[25,26,24,26,32,36,24,56,24,85,15,26],
    "PR":[85,92,98,78,93,94,86,96,87,32,64,99],
    "marks":[98,94,98,90,98,96,98,98,97,91,92,95]
}

df= pd.DataFrame(data)
print(df)

print("Update columns")

df.loc[0, "PR"]= 96
print(df)

print("whole column update")

df["PR"]= df["PR"]*1.25
print(df)