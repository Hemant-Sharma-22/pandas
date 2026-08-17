import pandas as pd

data= {
    "name": ["ram", "shyam","gopinath", "ghanshyam","Mohan","krishna","pritam", "pyare","devkinandan","baanke","madav","gopal"],
    "age":[25,26,24,26,32,36,24,56,24,85,15,26],
    "PR":[85,92,98,78,93,54,86,96,87,32,64,99],
    "marks":[98,94,98,90,98,96,98,98,97,91,92,95]
}

df= pd.DataFrame(data)
print(df)

#using assignment square brackets
df["Before 5 Years"]= df["age"] - 5
print(df)

#using insert() method
df.insert(0,"emp_id", [1,2,3,4,5,6,7,8,9,10,11,12])
print(df)