# '''
#     1. selection of specific column -> using square brackets -> return series and dataFrame
#     2. filtering rows -> df[df["column_Name] > 500000], 
#                         Another way when multiple conditions df[(df["column_Name] > 500000) & (df["column_Name] < 800000)]
# '''

import pandas as pd

data= {
    "name": ["ram", "shyam","gopinath", "ghanshyam","Mohan","krishna","pritam", "pyare","devkinandan","baanke","madav","gopal"],
    "age":[25,26,24,26,32,36,24,56,24,85,15,26],
    "PR":[85,92,98,78,93,54,86,96,87,32,64,99],
    "marks":[98,94,98,90,98,96,98,98,97,91,92,95]
}

df= pd.DataFrame(data)
print(df)

print("Selecting specific columns")
subset= df[["name", "PR"]]
print(subset)

print("Filtering rows")
print(df[ (df["PR"]>64) & (df["marks"] < 95) ])
