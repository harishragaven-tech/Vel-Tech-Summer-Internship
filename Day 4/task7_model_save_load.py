import pickle
from pathlib import Path

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

model_path = script_dir / "stress_model.pkl"

with open(model_path, "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")

with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

print("Model loaded successfully!")

new_student = pd.DataFrame(
    [[20, 5, 4, 3]],
    columns=["Age", "Depression_Score", "Anxiety_Score", "Financial_Stress"],
)

prediction = loaded_model.predict(new_student)

print("Predicted Stress Level:", prediction[0])