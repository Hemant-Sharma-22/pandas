import pandas as pd

data= {
    "name": ["ram",None,"gopinath", "ghanshyam","Mohan","krishna","pritam", "pyare","devkinandan","baanke","madav","gopal"],
    "age":[25,None,24,26,32,36,24,56,24,85,15,26],
    "PR":[85,None,98,78,93,54,86,96,87,32,64,99],
    "marks":[98,None,98,90,98,96,98,98,97,91,92,95]
}

df= pd.DataFrame(data)
print(df)

print(df.isnull().sum())