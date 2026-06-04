from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "students_mental_health_survey.csv"

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")


df = pd.read_csv(csv_path)
gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(8, 5))
bars = plt.bar(
    gender_counts.index,
    gender_counts.values,
    color=["skyblue", "lightgreen"],
)
plt.title("Gender Distribution of Students")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.grid(axis="y", linestyle="--")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(height),
        ha="center",
        va="bottom",
    )

plt.tight_layout()
plt.savefig(script_dir / "custom_gender_chart.png", dpi=150)
plt.close()