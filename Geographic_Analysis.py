import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Using a clean background style for the coordinate plot
sns.set_style("whitegrid")

# Load the restaurant dataset
# Assumes the 'Dataset.csv' file is in the same directory
restaurant_df = pd.read_csv('Dataset.csv')

# --- INITIALIZING THE GEOGRAPHIC PLOT ---
# We're using a scatter plot where X is Longitude and Y is Latitude
# This essentially builds a custom map of restaurant locations
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the points
# s=20: keeps dots small enough to see individual points
# alpha=0.4: allows dots to overlap so we can spot high-density 'hotspots'
sns.scatterplot(
    data=restaurant_df, 
    x='Longitude', 
    y='Latitude', 
    hue='City', 
    palette='viridis', 
    legend=False, 
    alpha=0.4, 
    s=25,
    ax=ax
)

# --- POLISHING THE VISUALS ---
ax.set_title('Mapping Restaurant Clusters via Coordinates', fontsize=15, weight='bold', pad=15)
ax.set_xlabel('Longitude', fontsize=11)
ax.set_ylabel('Latitude', fontsize=11)

# Adding dashed grid lines to make the coordinate zones easier to track
ax.grid(True, linestyle=':', alpha=0.5)

# Finalizing the layout for display
plt.tight_layout()
plt.show()

# --- ANALYTICAL INSIGHT ---
# Calculating which city has the highest concentration of restaurants mathematically
city_tally = restaurant_df['City'].value_counts()
top_cluster_city = city_tally.idxmax()
top_cluster_count = city_tally.max()

print(f"Analysis Result: The most dense restaurant cluster is {top_cluster_city} with {top_cluster_count} listings.")