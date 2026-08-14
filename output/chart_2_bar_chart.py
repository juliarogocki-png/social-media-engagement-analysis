"""
Chart 2: Bar Chart – Top 5 Posts by Score
Social Media Engagement Analysis

Output: output/chart_2_bars.png
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
palette = sns.color_palette("muted")

# ============================================================
# CHART 2: Bar Chart – Top 5 Posts by Score
# ============================================================
plt.figure(figsize=(10, 6))

top5 = df.nlargest(5, "score").sort_values("score")

plt.barh(
    top5["title"].str[:30] + "...",
    top5["score"],
    color=palette[2]
)

plt.title("Top 5 Posts by Upvotes", fontsize=14, fontweight="600")
plt.xlabel("Score", fontsize=12)
plt.ylabel("Post Title", fontsize=12)
plt.tight_layout()

# Speichern im output-Ordner
plt.savefig("output/chart_2_bars.png", dpi=150)
plt.close()

print("✅ Chart 2 erstellt: output/chart_2_bars.png")
