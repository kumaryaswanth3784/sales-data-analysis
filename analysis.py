import pandas as pd 
df=pd.read_csv("sales.csv")
print("Sales Data")
print(df)
print("\nTotal Sales:")
print(df["amount"].sum())

print("\nCategory Wise Sales:")
print(df.groupby("category")["amount"].sum())