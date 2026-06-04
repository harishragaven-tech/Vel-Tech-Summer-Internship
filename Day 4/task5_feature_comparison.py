from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "students_mental_health_survey.csv"

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")


df = pd.read_csv(csv_path)

features = [
    "Age",
    "Depression_Score",
    "Anxiety_Score",
    "Financial_Stress"
]

target = "Stress_Level"

for feature in features:

    X = df[[feature]]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    print(feature, "MSE =", round(mse, 4))