import pandas as pd

data = {
    "Name": ["Arun", "Ganesh", "Raghul", "Manoj", "Karthik"],
    "Age": [18, 19, 20, 20, 19],
    "City": ["Chennai", "Madurai", "Coimbatore", "Karur", "Trichy"],
    "Marks": [85, 76, 90, 64, 78]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nShape:", df.shape)
print("\nData Types:")
print(df.dtypes)

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nUpdated DataFrame:")
print(df)