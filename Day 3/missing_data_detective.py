import pandas as pd
from pathlib import Path

# ── STEP 1: Load the CSV ─────────────────────────────────────
csv_path = Path(__file__).resolve().parent / "students_mental_health_survey.csv"
df = pd.read_csv(csv_path)

print("=" * 50)
print("STEP 1: Dataset Loaded")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("=" * 50)

# ── STEP 2: Find columns with nulls & how many ──────────────
print("\nSTEP 2: Columns with Missing Values")
print("-" * 40)
missing = df.isnull().sum()
missing_cols = missing[missing > 0]

if missing_cols.empty:
    print("No missing values found!")
else:
    for col, count in missing_cols.items():
        print(f"  {col}: {count} missing value(s)")

print(f"\nTotal missing values: {df.isnull().sum().sum()}")

# ── STEP 3: Fill numeric nulls with column mean ──────────────
print("\nSTEP 3: Filling Numeric Nulls with Column Mean")
print("-" * 40)
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        mean_val = round(df[col].mean(), 2)
        df[col].fillna(mean_val, inplace=True)
        print(f"  '{col}' filled with mean = {mean_val}")

# ── STEP 4: Fill text nulls with 'Unknown' ───────────────────
print("\nSTEP 4: Filling Text Nulls with 'Unknown'")
print("-" * 40)
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna("Unknown", inplace=True)
        print(f"  '{col}' filled with 'Unknown'")

# ── STEP 5: Verify no nulls remain ───────────────────────────
print("\nSTEP 5: Verifying No Nulls Remain")
print("-" * 40)
remaining_nulls = df.isnull().sum().sum()

if remaining_nulls == 0:
    print(" All missing values have been filled!")
    print(" Dataset is now complete and clean.")
else:
    print(f"{remaining_nulls} null(s) still remain — check manually.")

print("\n" + "=" * 50)
print("TASK 4 COMPLETE — Missing Data Detective")
print("=" * 50)
