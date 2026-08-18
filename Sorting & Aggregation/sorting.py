# using   .sort_values(by ="column_name", ascending= True/False, inplace= True)
import pandas as pd

data={
    "name":["Avinash","Aviral","Banke","Shivaji"],
    "age":[25,64,78,36],
    "marks":[54,65,55,62]
}

df= pd.DataFrame(data)
print(df)

# print("sort single column")
# df.sort_values(by= "age", ascending=True, inplace= True)
# print(df)

print("multiple column")
df.sort_values(by= ["age", "marks"], ascending=[True, True], inplace= True)
print(df)