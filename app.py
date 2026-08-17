import pandas as pd # type: ignore
import sys

sys.stdout.reconfigure(encoding="UTF-8")

data= pd.read_excel("tests-example.xls", engine="xlrd")

print(data.head())
