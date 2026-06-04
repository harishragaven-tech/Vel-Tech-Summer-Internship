from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "students_mental_health_survey.csv"

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")


df = pd.read_csv(csv_path)

X = df[["Age", "Depression_Score", "Anxiety_Score", "Financial_Stress"]]
y = df["Stress_Level"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)
pd.DataFrame(
    [[20, 5, 4, 3]],
    columns=["Age", "Depression_Score", "Anxiety_Score", "Financial_Stress"],
)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2 Score:", r2)

new_student = [[20, 5, 4, 3]]
prediction = model.predict(new_student)

print("Predicted Stress Level:", prediction[0])