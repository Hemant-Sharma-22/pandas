# pd.merge(df1, df2, on="column_name", how="type of join")

import pandas as pd

df_shop= pd.DataFrame({
    "cus_id":[1,2,3],
    "goods":["sugar","oil","fig"]
})


df_user= pd.DataFrame({
    "cus_id":[1,2,4],
    "name":["sagar","om","prem"]
})

df_merge= pd.merge(df_user,df_shop, on="cus_id", how="inner")
print("inner join")
print(df_merge)