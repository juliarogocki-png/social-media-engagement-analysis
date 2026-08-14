"""
Download Dataset from Kaggle
Social Media Engagement Analysis

This script downloads the real dataset from Kaggle
and saves it as data.csv in the project folder.

Author: Julia Rogocki
Date: August 2026
"""

import kagglehub
import os
import pandas as pd

# ============================================================
# Get the directory where this script is located
# ============================================================
script_dir = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# STEP 1: Download dataset from Kaggle
# ============================================================
print("📥 Downloading dataset from Kaggle...")
print("Dataset: subashmaster0411/social-media-engagement-dataset")
print()

# Download the dataset
path = kagglehub.dataset_download("subashmaster0411/social-media-engagement-dataset")

print("✅ Dataset downloaded successfully!")
print(f"📁 Location: {path}")
print()

# ============================================================
# STEP 2: Find CSV file(s) in downloaded dataset
# ============================================================
print("🔍 Looking for CSV files in dataset...")
dataset_files = os.listdir(path)
print(f"Files found: {dataset_files}")
print()

# Find CSV files
csv_files = [f for f in dataset_files if f.endswith('.csv')]

if not csv_files:
    print("❌ No CSV files found in dataset!")
    print("Please check the dataset manually on Kaggle.")
else:
    print(f"✅ Found {len(csv_files)} CSV file(s): {csv_files}")
    print()
    
    # ============================================================
    # STEP 3: Load and prepare data
    # ============================================================
    # Use the first CSV file (or you can specify which one)
    csv_file = csv_files[0]
    csv_path = os.path.join(path, csv_file)
    
    print(f"📖 Loading: {csv_file}")
    df = pd.read_csv(csv_path)
    
    print(f"📊 Dataset shape: {df.shape}")
    print(f"📋 Columns: {list(df.columns)}")
    print()
    
    # ============================================================
    # STEP 4: Select/rename columns for our analysis
    # ============================================================
    print("🔧 Preparing data for analysis...")
    
    # Check what columns we have and map them to our expected columns
    # Expected: title, score, num_comments, created, subreddit, upvote_ratio
    
    # Create a new dataframe with our expected columns
    df_new = pd.DataFrame()
    
    # Try to map common column names
    column_mapping = {
        'title': ['title', 'text', 'content', 'post', 'post_text'],
        'score': ['score', 'likes', 'upvotes', 'reactions', 'engagement'],
        'num_comments': ['num_comments', 'comments', 'numcomments', 'comment_count'],
        'created': ['created', 'date', 'timestamp', 'created_at', 'post_date'],
        'subreddit': ['subreddit', 'platform', 'category', 'source', 'community'],
        'upvote_ratio': ['upvote_ratio', 'engagement_rate', 'ratio', 'rate']
    }
    
    for new_col, possible_names in column_mapping.items():
        for col_name in possible_names:
            if col_name in df.columns:
                df_new[new_col] = df[col_name]
                print(f"  ✓ Mapped '{col_name}' → '{new_col}'")
                break
        else:
            # Column not found, create with default/placeholder
            if new_col == 'title':
                df_new[new_col] = [f"Post_{i}" for i in range(len(df))]
            elif new_col == 'score':
                df_new[new_col] = 0
            elif new_col == 'num_comments':
                df_new[new_col] = 0
            elif new_col == 'created':
                df_new[new_col] = pd.Timestamp.now()
            elif new_col == 'subreddit':
                df_new[new_col] = 'unknown'
            elif new_col == 'upvote_ratio':
                df_new[new_col] = 0.5
            print(f"  ⚠ Created placeholder for '{new_col}'")
    
    print()
    
    # ============================================================
    # STEP 5: Save as data.csv in SAME FOLDER as this script
    # ============================================================
    output_file = os.path.join(script_dir, "data.csv")
    print(f"💾 Saving prepared data as '{output_file}'...")
    
    df_new.to_csv(output_file, index=False)
    
    print(f"✅ Data saved successfully!")
    print(f"📁 File: {output_file}")
    print(f"📊 Shape: {df_new.shape}")
    print()
    
    # ============================================================
    # STEP 6: Show sample data
    # ============================================================
    print("📋 First 5 rows of prepared data:")
    print(df_new.head())
    print()
    
    print("=" * 60)
    print("🎉 DONE! You can now run your analysis scripts:")
    print("=" * 60)
    print()
    print("  python chart_1_scatter_plot.py")
    print("  python chart_2_bar_chart.py")
    print("  python chart_3_heatmap.py")
    print()
    print("  OR all at once:")
    print("  python run_all_charts.py")
    print()
