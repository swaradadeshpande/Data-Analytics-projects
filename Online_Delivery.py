import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Applying a standard grid theme for the plots
sns.set_style("whitegrid")

# Loading dataset
zomato_data = pd.read_csv('Dataset.csv')

# --- 1. Checking Online Delivery Adoption ---
delivery_stats = zomato_data['Has Online delivery'].value_counts()

# Converting those counts into percentages
online_pct = (delivery_stats['Yes'] / len(zomato_data)) * 100

# --- 2. Comparing Quality vs. Delivery ---
rating_comparison = zomato_data.groupby('Has Online delivery')['Aggregate rating'].mean()

# Displaying the results in the console
print(f"Stats: {online_pct:.2f}% of restaurants offer online delivery.")
print("-" * 30)
print(f"Mean Rating (With Delivery): {rating_comparison['Yes']:.2f}")
print(f"Mean Rating (No Delivery): {rating_comparison['No']:.2f}")

# --- 3. Creating the Comparison Chart ---
# figure size for the plot
plt.figure(figsize=(8, 5))

# Plotting the average ratings as a bar chart
delivery_plot = sns.barplot(
    x=rating_comparison.index, 
    y=rating_comparison.values, 
    palette=['#e67e22', '#2980b9'], 
    edgecolor='0.3'
)

# Adding clear titles and descriptive axis labels
plt.title('How Online Delivery Affects Ratings', fontsize=13, weight='bold')
plt.xlabel('Online Delivery Service?', fontsize=11)
plt.ylabel('Average Rating Score', fontsize=11)

plt.ylim(0, 5)

for index, rating in enumerate(rating_comparison):
    delivery_plot.text(
        index, rating + 0.1, 
        f'{rating:.2f}', 
        ha='center', 
        fontweight='bold', 
        color='black'
    )

#final graph
plt.tight_layout()
plt.show()