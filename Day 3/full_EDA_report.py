import pandas as pd
from pathlib import Path

# ── EDA FUNCTION ─────────────────────────────────────────────
def eda_report(df):
    """
    Takes any DataFrame and prints:
    - Shape
    - Null counts
    - describe() for numeric columns
    - value_counts() for object (text) columns
    """
    print("=" * 60)
    print("FULL EDA REPORT")
    print("=" * 60)

    # 1. Shape
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")

    # 2. Nulls
    print("\nMissing Values (Nulls):")
    print("-" * 40)
    nulls = df.isnull().sum()
    null_cols = nulls[nulls > 0]
    if null_cols.empty:
        print("No missing values found!")
    else:
        for col, count in null_cols.items():
            print(f"  {col}: {count} missing")
    print(f"  Total nulls: {nulls.sum()}")

    # 3. describe() for numeric columns
    numeric_cols = df.select_dtypes(include='number')
    if not numeric_cols.empty:
        print("\nNumeric Columns — Statistical Summary:")
        print("-" * 40)
        print(numeric_cols.describe().round(2).to_string())

    # 4. value_counts() for object columns
    object_cols = df.select_dtypes(include=['object', 'string'])
    if not object_cols.empty:
        print("\n Text/Categorical Columns — Value Counts:")
        print("-" * 40)
        for col in object_cols.columns:
            print(f"\n{col}:")
            print(df[col].value_counts().to_string(header=False))

    print("\n" + "=" * 60)
    print("EDA REPORT COMPLETE")
    print("=" * 60)


# ── TEST ON CSV 1: Full dataset ───────────────────────────────
csv_path = Path(__file__).resolve().parent / "students_mental_health_survey.csv"

print("\n>>> Testing on: students_mental_health_survey (Full Dataset)")
df1 = pd.read_csv(csv_path)
eda_report(df1)


# ── TEST ON CSV 2: Subset (first 100 rows) ────────────────────
print("\n\n>>> Testing on: students_mental_health_survey (First 100 Rows Subset)")
df2 = pd.read_csv(csv_path, nrows=100)
eda_report(df2)