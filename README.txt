=================================================================
SOCIAL MEDIA ENGAGEMENT ANALYSIS
Data Analysis Portfolio Project
=================================================================

AUTHOR: Julia Rogocki
DATE: August 2026
GITHUB: https://github.com/juliarogocki-png/social-media-engagement-analysis

=================================================================
PROJECT OVERVIEW
=================================================================

An exploratory data analysis examining which factors influence 
engagement rates on social media posts, using Python for clear 
visualizations and reproducible insights.

Focus: Social media analytics, engagement patterns, Python visualization
Role: End-to-end analysis, data preparation, chart design, portfolio documentation

=================================================================
RESEARCH QUESTION
=================================================================

Primary Question:
Which factors influence the engagement rate of social media posts?

Sub-questions:
1. Do posts with more upvotes also generate more comments?
2. Are there differences in engagement patterns across subreddits?
3. Which metrics capture distinct vs. redundant engagement dimensions?

=================================================================
DATASET
=================================================================

Sample dataset of 10 Reddit posts with fields:
- title (string): Post title
- score (integer): Upvote count
- num_comments (integer): Number of comments
- created (date): Creation date
- subreddit (string): Community name
- upvote_ratio (float): Upvote ratio (0-1)

=================================================================
VISUALIZATIONS
=================================================================

Three separate charts, each in its own script:

1. CHART 1: Scatter Plot (Score vs. Comments)
   File: chart_1_scatter_plot.py
   Output: output/chart_1_scatter.png
   Purpose: Test if high-scoring posts also generate discussion

2. CHART 2: Bar Chart (Top 5 Posts)
   File: chart_2_bar_chart.py
   Output: output/chart_2_bars.png
   Purpose: Identify highest-performing content

3. CHART 3: Heatmap (Correlation Matrix)
   File: chart_3_heatmap.py
   Output: output/chart_3_heatmap.png
   Purpose: Show relationships between engagement metrics

=================================================================
PROJECT STRUCTURE
=================================================================

social-media-engagement-analysis/
|
+-- output/                          # Generated charts (after running scripts)
|   +-- chart_1_scatter.png          # Scatter plot
|   +-- chart_2_bars.png             # Bar chart
|   +-- chart_3_heatmap.png          # Heatmap
|
+-- chart_1_scatter_plot.py          # Script for Chart 1
+-- chart_2_bar_chart.py             # Script for Chart 2
+-- chart_3_heatmap.py               # Script for Chart 3
+-- run_all_charts.py                # Run all 3 charts at once
+-- social-media-analysis.html       # Project page for GitHub Pages
+-- requirements.txt                 # Python dependencies
+-- .gitignore                       # Git ignore rules
+-- README.txt                       # This file

=================================================================
INSTALLATION
=================================================================

Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)

Step 1: Clone or download repository

Step 2: Create virtual environment (recommended)
   Windows:
   python -m venv venv
   venv\Scripts\activate
   
   macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

Step 3: Install dependencies
   pip install -r requirements.txt

Dependencies:
- pandas>=2.0.0
- seaborn>=0.12.0
- matplotlib>=3.7.0

=================================================================
USAGE
=================================================================

OPTION A: Run individual chart scripts
---------------------------------------
python chart_1_scatter_plot.py    # Creates output/chart_1_scatter.png
python chart_2_bar_chart.py       # Creates output/chart_2_bars.png
python chart_3_heatmap.py         # Creates output/chart_3_heatmap.png

OPTION B: Run all charts at once
---------------------------------
python run_all_charts.py

This executes all three scripts sequentially and creates all charts
in the output/ folder.

OPTION C: View project page
----------------------------
Open social-media-analysis.html in your browser

Windows: start social-media-analysis.html
macOS: open social-media-analysis.html
Linux: xdg-open social-media-analysis.html

=================================================================
KEY INSIGHTS
=================================================================

Finding 1: Engagement Metrics Are Related But Distinct
- Score and comments are moderately correlated (r ≈ 0.4-0.6)
- High-scoring posts tend to have more comments, but not always

Finding 2: Subreddit Culture Matters
- Photography: High scores, moderate comments (visual appreciation)
- Learning/UX: Moderate scores, high comments (discussion-driven)
- Academic: Lower scores, fewer comments (niche audience)

Finding 3: Top Content Is Diverse
- High-performing posts span multiple topics
- Quality and relevance matter more than topic alone

=================================================================
TECHNOLOGIES
=================================================================

Technology    Version    Purpose
Python        3.8+       Programming language
pandas        2.0+       Data manipulation
seaborn       0.12+      Statistical visualization
matplotlib    3.7+       Plotting backend
Git           -          Version control
GitHub        -          Repository hosting
GitHub Pages  -          Static site hosting

=================================================================
PORTFOLIO RELEVANCE
=================================================================

This project demonstrates:
✓ Research Design: Clear, answerable questions
✓ Data Wrangling: Loading and transforming tabular data
✓ Visualization: Appropriate chart types for different insights
✓ Technical Communication: Clean, documented code
✓ Sociological Perspective: Connecting patterns to social behavior

Relevance for:
- UX Research: Understanding user engagement
- Digital Sociology: Analyzing online behavior
- Data Analysis: Python, pandas, visualization skills

=================================================================
GITHUB PAGES SETUP (OPTIONAL)
=================================================================

1. Go to your repo on GitHub
2. Click: Settings → Pages
3. Source: Deploy from a branch
4. Branch: main, Folder: / (root)
5. Click: Save
6. Wait 2-3 minutes

Live URL:
https://juliarogocki-png.github.io/social-media-engagement-analysis/social-media-analysis.html

=================================================================
NEXT STEPS
=================================================================

Short-term:
- Replace sample data with real Reddit API data
- Increase sample size (100+ posts)
- Add time-series analysis
- Include text analysis of titles

Medium-term:
- Interactive dashboard with Plotly/Streamlit
- Filters for subreddit, date range
- Multi-platform comparison

Long-term:
- Integrate into larger analytics portfolio
- Connect to Master's thesis research
- Use in job applications

=================================================================
AUTHOR
=================================================================

Julia Rogocki
Master's Student in Sociology | UX Research & Data Analysis
Location: Aachen, North Rhine-Westphalia, Germany

GitHub: https://github.com/juliarogocki-png
Portfolio: https://juliarogocki-png.github.io

Interests:
- UX Research
- Digital Product Design
- Social Media Analytics
- Organizational Sociology
- Process Digitalization

=================================================================
LICENSE
=================================================================

MIT License - Open Source
See full license text in project repository.

=================================================================
ACKNOWLEDGMENTS
=================================================================

- Data: Sample dataset inspired by Reddit posts
- Inspiration: DataCamp, Kaggle, data analytics portfolios
- Tools: Python data science stack

=================================================================
Last updated: 14.08.2026
Project version: 2.0 (modular scripts)
=================================================================