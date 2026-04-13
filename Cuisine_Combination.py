import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Applying a clean theme for the visuals
sns.set_context("notebook")
sns.set_style("ticks")

# Load the restaurant dataset
# Make sure your CSV file is in the same folder as this script
df_restaurants = pd.read_csv('Dataset.csv')

# --- DATA CLEANING ---
# Removing any entries that don't have cuisine information to keep the data reliable
valid_cuisine_data = df_restaurants.dropna(subset=['Cuisines']).copy()

# --- STEP 1: FINDING FREQUENT CUISINE PAIRINGS ---
# We want to see which cuisine combinations appear most often
# I'm extracting the top 10 most common strings here
top_10_combos = valid_cuisine_data['Cuisines'].value_counts().nlargest(10)

# --- STEP 2: RATING ANALYSIS BY COMBINATION ---
# Now we calculate the average rating for just these top 10 combinations
# First, filter the main list to only include these specific pairings
target_names = top_10_combos.index
subset_df = valid_cuisine_data[valid_cuisine_data['Cuisines'].isin(target_names)]

# Grouping by the cuisine string and calculating the mean score
combo_performance = subset_df.groupby('Cuisines')['Aggregate rating'].mean()

# Aligning the rating order with our frequency counts
combo_performance = combo_performance.reindex(target_names)

# Printing a summary to the console for a quick check
print(">>> Summary: Top 10 Cuisine Combinations & Ratings <<<")
for combo, count in top_10_combos.items():
    avg_score = combo_performance[combo]
    print(f"Combination: {combo} | Outlets: {count} | Avg Score: {avg_score:.2f}")

# --- STEP 3: CREATING THE VISUALIZATION ---
# Setting up the plot dimensions
plt.figure(figsize=(13, 8))

# Drawing the horizontal bar chart
# I'm using the 'viridis' color map as it looks very professional
chart_axis = sns.barplot(
    x=top_10_combos.values, 
    y=top_10_combos.index, 
    palette='viridis', 
    edgecolor='black',
    linewidth=0.8
)

# Customizing the look of the chart
plt.title('Top 10 Cuisine Combinations: Frequency vs Quality', fontsize=14, weight='bold')
plt.xlabel('Number of Restaurants', fontsize=11)
plt.ylabel('Cuisine Combination', fontsize=11)

# Adding the exact average rating next to each bar
for i, tally in enumerate(top_10_combos.values):
    current_rating = combo_performance.iloc[i]
    # Adding text labels slightly offset to the right
    chart_axis.text(
        tally + 10, 
        i, 
        f'Avg: {current_rating:.2f}', 
        va='center', 
        fontweight='bold', 
        color='darkred',
        fontsize=9
    )

# Tidying up the layout and displaying the plot
plt.tight_layout()
plt.show()