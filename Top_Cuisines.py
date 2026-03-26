import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Basic styling for the plots
sns.set_style("whitegrid")

# Load the restaurant dataset
# Make sure the CSV file is in your working directory
raw_data = pd.read_csv('Dataset.csv')

# --- DATA PREP ---
# Getting rid of entries where cuisine info is missing to avoid errors during splitting
clean_set = raw_data.dropna(subset=['Cuisines'])

# Since some restaurants list multiple cuisines, we split them by the comma
# and use explode to treat each one as a separate entry for counting
individual_cuisines = clean_set['Cuisines'].str.split(', ').explode()

# --- CALCULATING THE STATS ---
# Counting the frequency and picking the top three
top_3_list = individual_cuisines.value_counts().nlargest(3)

# Calculating what percentage of the total dataset these three represent
total_count = len(raw_data)
cuisine_percentages = (top_3_list / total_count) * 100

# --- CHARTING THE RESULTS ---
# Initializing the plot area
fig, ax = plt.subplots(figsize=(10, 6))

# Define custom colors to make the bar chart stand out
custom_colors = ['#ffadad', '#ffd6a5', '#fdffb6'] 

# Plotting the data
top_3_list.plot(kind='bar', ax=ax, color=custom_colors, edgecolor='grey', linewidth=1.2)

# Formatting the labels and titles to make them professional
ax.set_title('Market Overview: Most Common Cuisines', fontsize=15, weight='bold', pad=15)
ax.set_ylabel('Total Number of Restaurants', fontsize=12)
ax.set_xlabel('Cuisine Type', fontsize=12)
plt.xticks(rotation=0, fontweight='medium')

# Adding text labels on top of the bars to show exact numbers and %
for index, value in enumerate(top_3_list):
    pct_label = f"{value}\n({cuisine_percentages.iloc[index]:.1f}%)"
    ax.text(index, value + 40, pct_label, ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.show()