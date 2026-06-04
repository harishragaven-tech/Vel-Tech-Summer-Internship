from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "students_mental_health_survey.csv"

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")


df = pd.read_csv(csv_path)

X = df[["Age", "Depression_Score", "Anxiety_Score", "Financial_Stress"]]
y = df["Stress_Level"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred)

plt.title("Actual vs Predicted Stress Level")
plt.xlabel("Actual Stress Level")
plt.ylabel("Predicted Stress Level")

plt.grid(True)
plt.tight_layout()
plt.savefig(script_dir / "actual_vs_predicted.png", dpi=150)
plt.close()