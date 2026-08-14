"""
Run All Charts
Social Media Engagement Analysis

Führt alle drei Chart-Skripte nacheinander aus.
Output: output/ Ordner mit 3 PNG-Dateien

Author: Julia Rogocki
Date: August 2026
"""

import subprocess
import os

print("=" * 60)
print("SOCIAL MEDIA ENGAGEMENT ANALYSIS")
print("Generating all 3 charts...")
print("=" * 60)
print()

# Output-Ordner erstellen
os.makedirs("output", exist_ok=True)

# Chart 1 ausführen
print("📊 Generating Chart 1: Scatter Plot...")
subprocess.run(["python", "chart_1_scatter_plot.py"], check=True)
print()

# Chart 2 ausführen
print("📊 Generating Chart 2: Bar Chart...")
subprocess.run(["python", "chart_2_bar_chart.py"], check=True)
print()

# Chart 3 ausführen
print("📊 Generating Chart 3: Heatmap...")
subprocess.run(["python", "chart_3_heatmap.py"], check=True)
print()

print("=" * 60)
print("✅ ALL CHARTS GENERATED SUCCESSFULLY!")
print("=" * 60)
print()
print("Output files:")
print("  - output/chart_1_scatter.png")
print("  - output/chart_2_bars.png")
print("  - output/chart_3_heatmap.png")
print()
