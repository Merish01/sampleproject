import pandas as pd
import numpy as np

df = pd.read_csv("StudentData.csv")
df = df.drop_duplicates()
print("\nDuplicates removed")
print("\nData Types:\n", df.dtypes)
df.columns = df.columns.str.strip().str.lower()
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df_clean = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print("\nOutliers removed (if any)")

print("\nCleaned Data:\n", df_clean.head())

df_clean.to_csv("cleaned_student_data.csv", index=False)

print("\nCorrelation:\n", df_clean.corr())

df_clean["hours_group"] = pd.cut(df_clean["hours"], bins=3)

grouped = df_clean.groupby("hours_group")["scores"].mean()

print("\nAverage Scores by Study Hours Group:\n", grouped)

df_clean.to_csv("cleaned_student_data.csv", index=False)

df.groupby("hours")
