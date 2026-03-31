import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Using a clean white grid for the background of my plots
sns.set_style("whitegrid")

# Load the restaurant data file
# Note: Ensure 'Dataset.csv' is in the same directory as this script
restaurant_data = pd.read_csv('Dataset.csv')

# --- Analyzing the Rating Trends ---
# I'm using the mode function to see which rating pops up most frequently
# Since mode returns a series, I'm grabbing the very first result
frequent_rating_score = restaurant_data['Aggregate rating'].mode()[0]

# --- Calculating Engagement ---
# Finding the average number of votes to see the general level of customer feedback
mean_votes = restaurant_data['Votes'].mean()

# Output the findings to the console
print(f"Summary Result 1: The most frequent rating is {frequent_rating_score}")
print(f"Summary Result 2: On average, restaurants receive {mean_votes:.2f} votes")

# --- Building the Distribution Plot ---
# Setting the size of the graph to be clear and readable
plt.figure(figsize=(10, 6))

# Creating a histogram to show how ratings are spread out
# I've increased the bins slightly for more detail and added a smooth KDE line
sns.histplot(restaurant_data['Aggregate rating'], bins=25, kde=True, color='cornflowerblue', edgecolor='white')

# Labeling the chart clearly for the final report
plt.title('How Restaurant Ratings are Distributed', fontsize=15, weight='bold', pad=15)
plt.xlabel('Rating Score (0 to 5)', fontsize=11)
plt.ylabel('Number of Restaurants', fontsize=11)

# I'm adding a dashed red line to show exactly where the average sits on the graph
avg_val = restaurant_data['Aggregate rating'].mean()
plt.axvline(avg_val, color='darkred', linestyle='--', linewidth=2, label=f'Overall Average: {avg_val:.2f}')

# Show the legend to identify the average line
plt.legend(loc='upper right')

# Cleaning up the padding and displaying the figure
plt.tight_layout()
plt.show()