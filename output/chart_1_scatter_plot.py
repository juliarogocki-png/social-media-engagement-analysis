"""
Chart 1: Scatter Plot – Score vs. Comments
Social Media Engagement Analysis

Output: output/chart_1_scatter.png
Author: Julia Rogocki
Date: August 2026
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# Output-Ordner erstellen
os.makedirs("output", exist_ok=True)

# Datensatz
csv_data = """title,score,num_comments,created,subreddit,upvote_ratio
"Amazing sunset photo",15234,342,2024-01-15,photography,0.94
"Tips for learning Python?",8921,567,2024-01-16,learnpython,0.91
"New study on social movements",12456,234,2024-01-17,sociology,0.89
"UX design best practices",9834,445,2024-01-18,UXDesign,0.92
"Data visualization examples",11234,389,2024-01-19,datascience,0.93
"Travel photography inspiration",7654,278,2024-01-20,travel,0.88
"Academic writing tips",6543,312,2024-01-21,AcademicWriting,0.87
"Portfolio review feedback",8765,423,2024-01-22,webdev,0.90
"Research methodology discussion",5432,198,2024-01-23,research,0.86
"Digital product design trends",10234,501,2024-01-24,productdesign,0.91"""

# Daten laden
df = pd.read_csv(StringIO(csv_data))

# Seaborn Style setzen
sns.set(style="whitegrid")

# ============================================================
# CHART 1: Scatter Plot – Score vs. Comments
# ============================================================
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="score",
    y="num_comments",
    hue="subreddit",
    s=100,
    palette="muted",
    alpha=0.7
)

plt.title("Engagement Patterns: Upvotes vs. Comments", fontsize=14, fontweight="600")
plt.xlabel("Score (Upvotes)", fontsize=12)
plt.ylabel("Number of Comments", fontsize=12)
plt.legend(title="Subreddit", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Speichern im output-Ordner
plt.savefig("output/chart_1_scatter.png", dpi=150)
plt.close()

print("✅ Chart 1 erstellt: output/chart_1_scatter.png")