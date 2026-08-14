"""
Chart 3: Heatmap – Correlation Matrix
Social Media Engagement Analysis

Output: output/chart_3_heatmap.png
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
# CHART 3: Heatmap – Correlation Matrix
# ============================================================
plt.figure(figsize=(8, 6))

# Korrelationsmatrix berechnen
corr_matrix = df[["score", "num_comments", "upvote_ratio"]].corr()

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="YlOrRd",
    vmin=-1,
    vmax=1,
    cbar_kws={"label": "Korrelation"}
)

plt.title("Korrelationsmatrix: Engagement-Faktoren", fontsize=14, fontweight="600")
plt.tight_layout()

# Speichern im output-Ordner
plt.savefig("output/chart_3_heatmap.png", dpi=150)
plt.close()

print("✅ Chart 3 erstellt: output/chart_3_heatmap.png")
