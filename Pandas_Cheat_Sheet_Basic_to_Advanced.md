# Pandas Cheat Sheet --- Basic to Advanced

A practical Pandas reference for data analysis, cleaning,
transformation, filtering, grouping, merging, time series, and
performance.

------------------------------------------------------------------------

## 1. Installation

``` bash
pip install pandas
```

Import:

``` python
import pandas as pd
```

Check version:

``` python
print(pd.__version__)
```

------------------------------------------------------------------------

# 2. Core Pandas Objects

Pandas mainly works with:

-   **Series** → 1-dimensional labeled data
-   **DataFrame** → 2-dimensional table

## Series

``` python
s = pd.Series([10, 20, 30, 40])
```

With custom index:

``` python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
```

## DataFrame

``` python
df = pd.DataFrame({
    "name": ["Ram", "Shyam", "Mohan"],
    "age": [25, 26, 30],
    "marks": [85, 90, 78]
})
```

------------------------------------------------------------------------

# 3. Creating DataFrames

From dictionary:

``` python
df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "age": [20, 21, 22]
})
```

From list of dictionaries:

``` python
data = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 21}
]

df = pd.DataFrame(data)
```

Empty DataFrame:

``` python
df = pd.DataFrame()
```

------------------------------------------------------------------------

# 4. Reading Data

## CSV

``` python
df = pd.read_csv("data.csv")
```

Useful options:

``` python
df = pd.read_csv(
    "data.csv",
    usecols=["name", "age"],
    nrows=100,
    encoding="utf-8"
)
```

## Excel

``` python
df = pd.read_excel("data.xlsx")
```

## JSON

``` python
df = pd.read_json("data.json")
```

## SQL

``` python
df = pd.read_sql("SELECT * FROM users", connection)
```

## Parquet

``` python
df = pd.read_parquet("data.parquet")
```

------------------------------------------------------------------------

# 5. Writing / Exporting Data

CSV:

``` python
df.to_csv("output.csv", index=False)
```

Excel:

``` python
df.to_excel("output.xlsx", index=False)
```

JSON:

``` python
df.to_json("output.json")
```

Parquet:

``` python
df.to_parquet("output.parquet")
```

------------------------------------------------------------------------

# 6. Inspecting Data

First rows:

``` python
df.head()
df.head(10)
```

Last rows:

``` python
df.tail()
df.tail(10)
```

Random rows:

``` python
df.sample(5)
```

Shape:

``` python
df.shape
```

Returns:

``` text
(rows, columns)
```

Column names:

``` python
df.columns
```

Index:

``` python
df.index
```

Data types:

``` python
df.dtypes
```

Detailed information:

``` python
df.info()
```

Statistical summary:

``` python
df.describe()
```

Summary including categorical columns:

``` python
df.describe(include="all")
```

Unique values:

``` python
df["name"].unique()
```

Number of unique values:

``` python
df["name"].nunique()
```

Value counts:

``` python
df["name"].value_counts()
```

------------------------------------------------------------------------

# 7. Selecting Columns

Single column → Series:

``` python
df["name"]
```

Multiple columns → DataFrame:

``` python
df[["name", "age"]]
```

Using attribute notation:

``` python
df.name
```

> Prefer `df["name"]` because it works reliably with column names
> containing spaces or special characters.

------------------------------------------------------------------------

# 8. Selecting Rows

## `loc` --- Label Based

``` python
df.loc[0]
```

Rows:

``` python
df.loc[0:3]
```

Specific rows and columns:

``` python
df.loc[0:3, ["name", "age"]]
```

## `iloc` --- Position Based

``` python
df.iloc[0]
```

Rows:

``` python
df.iloc[0:3]
```

Rows and columns:

``` python
df.iloc[0:3, 0:2]
```

------------------------------------------------------------------------

# 9. Filtering Rows

One condition:

``` python
df[df["age"] > 25]
```

Equal:

``` python
df[df["age"] == 25]
```

Not equal:

``` python
df[df["age"] != 25]
```

Greater than or equal:

``` python
df[df["marks"] >= 80]
```

Less than:

``` python
df[df["marks"] < 50]
```

Multiple conditions:

``` python
df[(df["age"] > 20) & (df["marks"] > 80)]
```

OR:

``` python
df[(df["age"] > 25) | (df["marks"] > 90)]
```

NOT:

``` python
df[~(df["age"] > 25)]
```

> Use `&` for AND and `|` for OR. Put each condition inside parentheses.

------------------------------------------------------------------------

# 10. `isin()`

Filter values from a list:

``` python
df[df["name"].isin(["Ram", "Mohan"])]
```

NOT in:

``` python
df[~df["name"].isin(["Ram", "Mohan"])]
```

------------------------------------------------------------------------

# 11. `between()`

``` python
df[df["age"].between(20, 30)]
```

------------------------------------------------------------------------

# 12. String Filtering

Contains:

``` python
df[df["name"].str.contains("ram", case=False, na=False)]
```

Starts with:

``` python
df[df["name"].str.startswith("A", na=False)]
```

Ends with:

``` python
df[df["name"].str.endswith("n", na=False)]
```

Convert to lowercase:

``` python
df["name"].str.lower()
```

Convert to uppercase:

``` python
df["name"].str.upper()
```

Strip spaces:

``` python
df["name"].str.strip()
```

Replace:

``` python
df["name"].str.replace("old", "new", regex=False)
```

------------------------------------------------------------------------

# 13. Adding Columns

``` python
df["bonus"] = 1000
```

Column based on another column:

``` python
df["total"] = df["marks"] + 10
```

Multiple-column calculation:

``` python
df["score"] = df["marks"] * df["age"]
```

------------------------------------------------------------------------

# 14. Updating Columns

``` python
df["marks"] = df["marks"] + 5
```

Using `loc`:

``` python
df.loc[df["marks"] < 40, "result"] = "Fail"
```

------------------------------------------------------------------------

# 15. Rename Columns

``` python
df.rename(columns={"marks": "score"}, inplace=True)
```

Rename all columns:

``` python
df.columns = ["name", "age", "score"]
```

------------------------------------------------------------------------

# 16. Drop Columns

``` python
df.drop(columns=["age"], inplace=True)
```

Drop multiple:

``` python
df.drop(columns=["age", "marks"], inplace=True)
```

------------------------------------------------------------------------

# 17. Drop Rows

By index:

``` python
df.drop(index=[0, 2])
```

Reset index after filtering:

``` python
df.reset_index(drop=True, inplace=True)
```

------------------------------------------------------------------------

# 18. Sorting

Ascending:

``` python
df.sort_values("marks")
```

Descending:

``` python
df.sort_values("marks", ascending=False)
```

Multiple columns:

``` python
df.sort_values(
    ["age", "marks"],
    ascending=[True, False]
)
```

Sort by index:

``` python
df.sort_index()
```

------------------------------------------------------------------------

# 19. Missing Values

Check missing values:

``` python
df.isna()
```

Count missing values:

``` python
df.isna().sum()
```

Total missing values:

``` python
df.isna().sum().sum()
```

Opposite:

``` python
df.notna()
```

Drop rows containing missing values:

``` python
df.dropna()
```

Drop columns containing missing values:

``` python
df.dropna(axis=1)
```

Drop rows where all values are missing:

``` python
df.dropna(how="all")
```

Fill missing values:

``` python
df["age"] = df["age"].fillna(0)
```

Fill with mean:

``` python
df["age"] = df["age"].fillna(df["age"].mean())
```

Fill with median:

``` python
df["age"] = df["age"].fillna(df["age"].median())
```

Forward fill:

``` python
df.ffill()
```

Backward fill:

``` python
df.bfill()
```

------------------------------------------------------------------------

# 20. Duplicates

Check duplicates:

``` python
df.duplicated()
```

Count duplicates:

``` python
df.duplicated().sum()
```

Remove duplicates:

``` python
df.drop_duplicates()
```

Based on selected columns:

``` python
df.drop_duplicates(subset=["name"])
```

------------------------------------------------------------------------

# 21. Data Types

Check:

``` python
df.dtypes
```

Convert type:

``` python
df["age"] = df["age"].astype(int)
```

Numeric conversion:

``` python
df["marks"] = pd.to_numeric(
    df["marks"],
    errors="coerce"
)
```

Datetime conversion:

``` python
df["date"] = pd.to_datetime(df["date"])
```

------------------------------------------------------------------------

# 22. Statistics

Count:

``` python
df["marks"].count()
```

Sum:

``` python
df["marks"].sum()
```

Mean:

``` python
df["marks"].mean()
```

Median:

``` python
df["marks"].median()
```

Mode:

``` python
df["marks"].mode()
```

Minimum:

``` python
df["marks"].min()
```

Maximum:

``` python
df["marks"].max()
```

Variance:

``` python
df["marks"].var()
```

Standard deviation:

``` python
df["marks"].std()
```

Quantile:

``` python
df["marks"].quantile(0.25)
df["marks"].quantile(0.50)
df["marks"].quantile(0.75)
```

------------------------------------------------------------------------

# 23. Understanding `describe()`

``` python
df.describe()
```

Typical output:

  Statistic   Meaning
  ----------- ---------------------------
  count       Number of non-null values
  mean        Average
  std         Standard deviation
  min         Minimum
  25%         Q1 / first quartile
  50%         Median / Q2
  75%         Q3 / third quartile
  max         Maximum

------------------------------------------------------------------------

# 24. Standard Deviation Formula

Population standard deviation:

\[ `\sigma `{=tex}= `\sqrt{\frac{\sum(x-\mu)^2}{N}}`{=tex} \]

Sample standard deviation:

\[ s = `\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}`{=tex} \]

Pandas uses sample standard deviation by default:

``` python
df["marks"].std()
```

Population standard deviation:

``` python
df["marks"].std(ddof=0)
```

------------------------------------------------------------------------

# 25. Quartiles

Q1 = 25%

Q2 = 50% = Median

Q3 = 75%

``` python
df["marks"].quantile(0.25)
df["marks"].quantile(0.50)
df["marks"].quantile(0.75)
```

Interquartile range:

``` python
q1 = df["marks"].quantile(0.25)
q3 = df["marks"].quantile(0.75)

iqr = q3 - q1
```

------------------------------------------------------------------------

# 26. `groupby()`

Basic:

``` python
df.groupby("department")["salary"].mean()
```

Multiple aggregations:

``` python
df.groupby("department")["salary"].agg(
    ["mean", "min", "max", "count"]
)
```

Multiple columns:

``` python
df.groupby("department").agg({
    "salary": "mean",
    "age": "max"
})
```

Named aggregation:

``` python
result = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    max_age=("age", "max"),
    employees=("name", "count")
)
```

------------------------------------------------------------------------

# 27. `value_counts()`

``` python
df["department"].value_counts()
```

As percentages:

``` python
df["department"].value_counts(normalize=True) * 100
```

------------------------------------------------------------------------

# 28. `agg()`

Single column:

``` python
df["salary"].agg(["mean", "min", "max"])
```

DataFrame:

``` python
df.agg({
    "salary": ["mean", "max"],
    "age": ["mean", "min"]
})
```

------------------------------------------------------------------------

# 29. `transform()`

`transform()` returns a result aligned with the original DataFrame.

Example:

``` python
df["dept_avg_salary"] = (
    df.groupby("department")["salary"]
      .transform("mean")
)
```

Useful for comparing each row against its group.

------------------------------------------------------------------------

# 30. `apply()`

Apply a function:

``` python
df["marks"].apply(lambda x: x + 5)
```

Create category:

``` python
df["grade"] = df["marks"].apply(
    lambda x: "A" if x >= 80 else "B"
)
```

> Prefer vectorized operations when possible because they are usually
> faster than `apply()`.

------------------------------------------------------------------------

# 31. `map()`

Map values:

``` python
mapping = {
    "M": "Male",
    "F": "Female"
}

df["gender"] = df["gender"].map(mapping)
```

------------------------------------------------------------------------

# 32. `replace()`

``` python
df["status"] = df["status"].replace({
    "Y": "Yes",
    "N": "No"
})
```

------------------------------------------------------------------------

# 33. `where()` and `mask()`

Keep values when condition is true:

``` python
df["marks"].where(df["marks"] >= 40, 0)
```

Replace values when condition is true:

``` python
df["marks"].mask(df["marks"] < 40, 0)
```

------------------------------------------------------------------------

# 34. `query()`

Instead of:

``` python
df[(df["age"] > 25) & (df["marks"] > 80)]
```

Use:

``` python
df.query("age > 25 and marks > 80")
```

With variable:

``` python
minimum_marks = 80

df.query("marks >= @minimum_marks")
```

------------------------------------------------------------------------

# 35. Combining DataFrames

## `concat()`

Rows:

``` python
result = pd.concat([df1, df2])
```

Reset index:

``` python
result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

Columns:

``` python
result = pd.concat([df1, df2], axis=1)
```

------------------------------------------------------------------------

# 36. `merge()`

SQL-style join:

``` python
result = pd.merge(
    df1,
    df2,
    on="id",
    how="inner"
)
```

Types:

``` text
inner
left
right
outer
cross
```

Left join:

``` python
pd.merge(df1, df2, on="id", how="left")
```

Multiple keys:

``` python
pd.merge(
    df1,
    df2,
    on=["id", "year"]
)
```

Different column names:

``` python
pd.merge(
    df1,
    df2,
    left_on="user_id",
    right_on="id"
)
```

------------------------------------------------------------------------

# 37. `join()`

Join using index:

``` python
df1.join(df2)
```

------------------------------------------------------------------------

# 38. `pivot()`

``` python
df.pivot(
    index="date",
    columns="product",
    values="sales"
)
```

------------------------------------------------------------------------

# 39. `pivot_table()`

Useful for aggregation:

``` python
pd.pivot_table(
    df,
    values="sales",
    index="region",
    columns="product",
    aggfunc="sum"
)
```

Multiple aggregations:

``` python
pd.pivot_table(
    df,
    values="sales",
    index="region",
    aggfunc=["sum", "mean"]
)
```

------------------------------------------------------------------------

# 40. `melt()`

Convert wide data to long format:

``` python
pd.melt(
    df,
    id_vars=["name"],
    var_name="subject",
    value_name="marks"
)
```

------------------------------------------------------------------------

# 41. Reshaping

Stack:

``` python
df.stack()
```

Unstack:

``` python
df.unstack()
```

Transpose:

``` python
df.T
```

------------------------------------------------------------------------

# 42. Index Operations

Set index:

``` python
df.set_index("id")
```

Reset index:

``` python
df.reset_index()
```

Check index:

``` python
df.index
```

Sort index:

``` python
df.sort_index()
```

------------------------------------------------------------------------

# 43. Datetime

Convert:

``` python
df["date"] = pd.to_datetime(df["date"])
```

Year:

``` python
df["date"].dt.year
```

Month:

``` python
df["date"].dt.month
```

Month name:

``` python
df["date"].dt.month_name()
```

Day:

``` python
df["date"].dt.day
```

Day name:

``` python
df["date"].dt.day_name()
```

Day of week:

``` python
df["date"].dt.dayofweek
```

Extract date components:

``` python
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
```

------------------------------------------------------------------------

# 44. Time Series

Set datetime index:

``` python
df = df.set_index("date")
```

Resample monthly:

``` python
df["sales"].resample("ME").sum()
```

Daily:

``` python
df["sales"].resample("D").sum()
```

Weekly:

``` python
df["sales"].resample("W").sum()
```

Common aliases include:

``` text
D   = day
W   = week
ME  = month end
QE  = quarter end
YE  = year end
h   = hour
min = minute
s   = second
```

------------------------------------------------------------------------

# 45. Rolling Window

Rolling average:

``` python
df["sales"].rolling(7).mean()
```

Rolling sum:

``` python
df["sales"].rolling(7).sum()
```

Rolling standard deviation:

``` python
df["sales"].rolling(7).std()
```

------------------------------------------------------------------------

# 46. Expanding Window

``` python
df["sales"].expanding().mean()
```

------------------------------------------------------------------------

# 47. Cumulative Operations

Cumulative sum:

``` python
df["sales"].cumsum()
```

Cumulative maximum:

``` python
df["sales"].cummax()
```

Cumulative minimum:

``` python
df["sales"].cummin()
```

Cumulative product:

``` python
df["sales"].cumprod()
```

------------------------------------------------------------------------

# 48. Correlation and Covariance

Correlation:

``` python
df["age"].corr(df["salary"])
```

Full correlation matrix:

``` python
df.corr(numeric_only=True)
```

Covariance:

``` python
df["age"].cov(df["salary"])
```

------------------------------------------------------------------------

# 49. Memory Usage

``` python
df.info(memory_usage="deep")
```

Total memory:

``` python
df.memory_usage(deep=True).sum()
```

------------------------------------------------------------------------

# 50. Duplicate Columns / Data Cleaning

Check column names:

``` python
print(df.columns.tolist())
```

Strip column whitespace:

``` python
df.columns = df.columns.str.strip()
```

Standardize names:

``` python
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)
```

------------------------------------------------------------------------

# 51. Handling Large CSV Files

Read only required columns:

``` python
df = pd.read_csv(
    "large.csv",
    usecols=["name", "age", "salary"]
)
```

Read in chunks:

``` python
for chunk in pd.read_csv("large.csv", chunksize=10000):
    print(chunk.shape)
```

Process each chunk:

``` python
result = []

for chunk in pd.read_csv("large.csv", chunksize=10000):
    filtered = chunk[chunk["salary"] > 50000]
    result.append(filtered)

final = pd.concat(result, ignore_index=True)
```

------------------------------------------------------------------------

# 52. Efficient Data Types

Use smaller numeric types when appropriate:

``` python
df["age"] = df["age"].astype("int8")
```

Categorical data:

``` python
df["department"] = df["department"].astype("category")
```

Check memory:

``` python
df.memory_usage(deep=True)
```

------------------------------------------------------------------------

# 53. Vectorization

Prefer:

``` python
df["total"] = df["price"] * df["quantity"]
```

Instead of:

``` python
df["total"] = df.apply(
    lambda row: row["price"] * row["quantity"],
    axis=1
)
```

Vectorized operations are generally faster for large datasets.

------------------------------------------------------------------------

# 54. Conditional Columns with `np.where`

``` python
import numpy as np

df["result"] = np.where(
    df["marks"] >= 40,
    "Pass",
    "Fail"
)
```

Multiple conditions:

``` python
df["grade"] = np.select(
    [
        df["marks"] >= 90,
        df["marks"] >= 75,
        df["marks"] >= 60
    ],
    ["A+", "A", "B"],
    default="C"
)
```

------------------------------------------------------------------------

# 55. MultiIndex

Create MultiIndex:

``` python
df = df.set_index(["department", "year"])
```

Select:

``` python
df.loc[("IT", 2026)]
```

Reset:

``` python
df.reset_index()
```

------------------------------------------------------------------------

# 56. Categorical Data

Create category:

``` python
df["gender"] = df["gender"].astype("category")
```

Categories:

``` python
df["gender"].cat.categories
```

Add category:

``` python
df["gender"] = df["gender"].cat.add_categories(["Other"])
```

------------------------------------------------------------------------

# 57. Window Functions

Shift:

``` python
df["previous_sales"] = df["sales"].shift(1)
```

Difference:

``` python
df["change"] = df["sales"].diff()
```

Percentage change:

``` python
df["growth"] = df["sales"].pct_change()
```

Rank:

``` python
df["rank"] = df["marks"].rank(ascending=False)
```

------------------------------------------------------------------------

# 58. Top / Bottom Values

Top rows:

``` python
df.nlargest(5, "salary")
```

Bottom rows:

``` python
df.nsmallest(5, "salary")
```

------------------------------------------------------------------------

# 59. Sampling

Random rows:

``` python
df.sample(10)
```

Random fraction:

``` python
df.sample(frac=0.1)
```

Reproducible sample:

``` python
df.sample(10, random_state=42)
```

------------------------------------------------------------------------

# 60. `read_csv()` Important Parameters

``` python
pd.read_csv(
    "data.csv",
    sep=",",
    header=0,
    names=None,
    usecols=None,
    dtype=None,
    nrows=None,
    skiprows=None,
    na_values=None,
    parse_dates=None,
    chunksize=None,
    encoding="utf-8"
)
```

Useful examples:

``` python
pd.read_csv("data.csv", encoding="utf-8")
pd.read_csv("data.csv", usecols=["name", "age"])
pd.read_csv("data.csv", nrows=100)
pd.read_csv("data.csv", chunksize=10000)
```

------------------------------------------------------------------------

# 61. Common Errors

## KeyError

``` python
df["Name"]
```

If actual column is `"name"`, this raises a `KeyError`.

Check:

``` python
print(df.columns)
```

## SettingWithCopyWarning

Prefer `.loc`:

``` python
df.loc[df["marks"] < 40, "result"] = "Fail"
```

instead of chained assignment.

## TypeError in conditions

Check data type:

``` python
df["salary"].dtype
```

Convert:

``` python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

------------------------------------------------------------------------

# 62. Common Interview Questions

### Series vs DataFrame

**Series:** 1D labeled data.

**DataFrame:** 2D labeled tabular data.

### `loc` vs `iloc`

`loc` → label based.

`iloc` → integer-position based.

### `merge` vs `concat`

`merge()` → combines DataFrames using matching keys/columns.

`concat()` → stacks DataFrames along rows or columns.

### `map` vs `apply`

`map()` → commonly used on a Series for element-wise mapping.

`apply()` → applies a function to Series or DataFrame rows/columns.

### `groupby`

Splits data into groups, applies operations, and combines results.

### `transform`

Returns results aligned with the original DataFrame.

------------------------------------------------------------------------

# 63. Most Important Methods --- Quick Revision

``` python
# Inspection
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.dtypes

# Selection
df["column"]
df[["col1", "col2"]]
df.loc[]
df.iloc[]

# Filtering
df[df["age"] > 25]
df[(df["age"] > 25) & (df["marks"] > 80)]
df["name"].isin(["Ram", "Mohan"])

# Cleaning
df.isna()
df.dropna()
df.fillna()
df.drop_duplicates()

# Transformation
df.rename()
df.astype()
df.apply()
df.map()
df.replace()

# Sorting
df.sort_values()
df.sort_index()

# Aggregation
df.sum()
df.mean()
df.median()
df.std()
df.min()
df.max()
df.quantile()

# Grouping
df.groupby()
df.agg()
df.transform()

# Combining
pd.concat()
pd.merge()
df.join()

# Reshaping
df.pivot()
pd.pivot_table()
pd.melt()

# Time series
pd.to_datetime()
df.resample()
df.rolling()

# Export
df.to_csv()
df.to_excel()
df.to_json()
df.to_parquet()
```

------------------------------------------------------------------------

# 64. Practical Data Analysis Workflow

A common Pandas workflow:

``` python
import pandas as pd

# 1. Load
df = pd.read_csv("data.csv")

# 2. Understand
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# 3. Check quality
print(df.isna().sum())
print(df.duplicated().sum())

# 4. Clean
df = df.drop_duplicates()
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)

# 5. Filter
filtered = df[df["salary"] > 50000]

# 6. Transform
df["annual_salary"] = df["monthly_salary"] * 12

# 7. Group
summary = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    employees=("name", "count")
)

# 8. Sort
summary = summary.sort_values(
    "avg_salary",
    ascending=False
)

# 9. Export
summary.to_csv("summary.csv")
```

------------------------------------------------------------------------

# 65. Pandas Cheat Sheet in One Mental Model

Think of Pandas in this order:

``` text
READ
 ↓
INSPECT
 ↓
SELECT
 ↓
FILTER
 ↓
CLEAN
 ↓
TRANSFORM
 ↓
GROUP
 ↓
MERGE
 ↓
RESHAPE
 ↓
ANALYZE
 ↓
EXPORT
```

### The 15 methods you should know first

``` text
read_csv()
head()
info()
describe()
shape
dtypes
loc[]
iloc[]
isna()
fillna()
drop_duplicates()
sort_values()
groupby()
merge()
to_csv()
```

------------------------------------------------------------------------

## Mini Example

``` python
import pandas as pd

df = pd.DataFrame({
    "name": ["Ram", "Shyam", "Mohan", "Sita"],
    "age": [25, 30, 22, 28],
    "marks": [85, 92, 67, 95]
})

# Select columns
print(df[["name", "marks"]])

# Filter
print(df[df["marks"] > 80])

# Multiple conditions
print(
    df[
        (df["age"] > 24) &
        (df["marks"] > 80)
    ]
)

# Statistics
print(df["marks"].mean())
print(df["marks"].std())
print(df["marks"].quantile(0.25))

# Sort
print(df.sort_values("marks", ascending=False))

# New column
df["passed"] = df["marks"] >= 40

print(df)
```

------------------------------------------------------------------------

## Final Revision

``` text
Series          → 1D data
DataFrame       → 2D table
loc             → label selection
iloc            → position selection
filtering       → boolean conditions
groupby         → group + aggregate
agg             → multiple aggregations
transform       → group result aligned to rows
merge           → SQL-style join
concat           → stack/combine
pivot_table     → summarize/reshape
melt            → wide → long
fillna          → handle missing values
drop_duplicates → remove duplicates
describe        → statistical summary
quantile        → percentile/quartile
rolling         → moving window calculations
apply           → custom function
vectorization   → fast column operations
```

**Tip:** Don't try to memorize everything at once. Master **read →
inspect → select → filter → clean → groupby → merge → reshape → analyze
→ export**, then move to advanced topics.
