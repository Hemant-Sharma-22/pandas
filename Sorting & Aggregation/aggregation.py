import pandas as pd

data={
    "name":["Avinash","Aviral","Banke","Shivaji"],
    "age":[25,64,78,36],
    "marks":[54,65,55,62]
}

df= pd.DataFrame(data)
print(df)

print("Aggregation:- ")
print(f'Total marks: ',df["marks"].sum())
print(f'Avg Age: ',df["age"].mean())