import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# I'm using seaborn for the styling to make the visuals look cleaner
sns.set_theme(style="whitegrid")

# Load our dataset - assuming it's in the current folder
data = pd.read_csv('Dataset.csv')

# --- Analyzing Restaurant Volume by City ---
# Let's count how many restaurants are in each city
city_tally = data['City'].value_counts()
most_frequent_city = city_tally.idxmax()
max_restaurants = city_tally.max()

# --- Checking Quality (Ratings) Across Cities ---
# Grouping the rows by city name and calculating the mean rating for each
avg_city_scores = data.groupby('City')['Aggregate rating'].mean()

# Finding the specific city that has the highest average rating
top_scoring_city = avg_city_scores.idxmax()
top_score_value = avg_city_scores.max()

# Printing out the main findings
print(f"Result 1: The city with the most restaurants is {most_frequent_city} with {max_restaurants} total.")
print(f"Result 2: The highest average rating ({top_score_value:.2f}) was found in {top_scoring_city}.")

# --- Visualizing the Top Performers ---
# Picking out the top 10 cities by rating to plot
top_10_cities = avg_city_scores.sort_values(ascending=False).head(10)

# Setting up the figure size
fig, ax = plt.subplots(figsize=(11, 6))

# Creating a horizontal bar chart
# I chose the 'magma' palette for a professional look
sns.barplot(x=top_10_cities.values, y=top_10_cities.index, palette='magma', ax=ax)

# Adding some polish to the chart with custom titles and labels
ax.set_title('Top 10 Cities: Average Restaurant Ratings', fontsize=14, weight='bold')
ax.set_xlabel('Average Score (0 - 5 Scale)', fontsize=11)
ax.set_ylabel('City Name', fontsize=11)

# Zooming in on the 4-5 range to make the comparison easier to see
ax.set_xlim(4, 5)

# Adding subtle grid lines on the x-axis for better readability
ax.grid(axis='x', linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()