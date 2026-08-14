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