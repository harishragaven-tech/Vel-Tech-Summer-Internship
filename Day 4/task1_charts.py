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

print(df.columns)


def save_chart(filename: str) -> None:
    plt.tight_layout()
    plt.savefig(script_dir / filename, dpi=150)
    plt.close()

plt.figure(figsize=(6, 4))
df.groupby("Gender")["CGPA"].mean().plot(kind="bar")
plt.title("Average CGPA by Gender")
plt.xlabel("Gender")
plt.ylabel("Average CGPA")
save_chart("bar_chart.png")

plt.figure(figsize=(6, 4))
plt.scatter(df["Stress_Level"], df["CGPA"])
plt.title("Stress Level vs CGPA")
plt.xlabel("Stress Level")
plt.ylabel("CGPA")
save_chart("scatter_plot.png")

plt.figure(figsize=(6, 4))
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
save_chart("histogram.png")

plt.figure(figsize=(6, 4))

scores = [
    df["Stress_Level"].mean(),
    df["Depression_Score"].mean(),
    df["Anxiety_Score"].mean()
]

labels = ["Stress", "Depression", "Anxiety"]

plt.plot(labels, scores, marker="o")
plt.title("Average Mental Health Scores")
plt.xlabel("Category")
plt.ylabel("Average Score")
save_chart("line_chart.png")

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(6, 4))
plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%")
plt.title("Gender Distribution")
save_chart("gender_pie_chart.png")

plt.figure(figsize=(6, 4))
df.groupby("Gender")["Stress_Level"].mean().plot(kind="bar")
plt.title("Average Stress Level by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Stress Level")
save_chart("stress_by_gender.png")

plt.figure(figsize=(6, 4))
plt.hist(df["Stress_Level"], bins=10)
plt.title("Stress Level Distribution")
plt.xlabel("Stress Level")
plt.ylabel("Frequency")
save_chart("stress_histogram.png")

plt.figure(figsize=(6, 4))
plt.scatter(df["Anxiety_Score"], df["Depression_Score"])
plt.title("Anxiety vs Depression")
plt.xlabel("Anxiety Score")
plt.ylabel("Depression Score")
save_chart("anxiety_vs_depression.png")

plt.figure(figsize=(6, 4))
df.groupby("Gender")["Anxiety_Score"].mean().plot(kind="bar")
plt.title("Average Anxiety Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Anxiety Score")
save_chart("anxiety_by_gender.png")

plt.figure(figsize=(6, 4))
plt.hist(df["Depression_Score"], bins=10)
plt.title("Depression Score Distribution")
plt.xlabel("Depression Score")
plt.ylabel("Frequency")
save_chart("depression_score_distribution.png")