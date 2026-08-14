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

# Output-Ordner erstellen
os.makedirs("output", exist_ok=True)

# ============================================================
# DATEN LADEN AUS CSV-DATEI (Kaggle Data)
# ============================================================
# Lade die echten Daten aus data.csv (von Kaggle heruntergeladen)
df = pd.read_csv("data.csv")

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
