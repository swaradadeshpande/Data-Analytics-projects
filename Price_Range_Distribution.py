import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Loading dataset
restaurant_data = pd.read_csv('Dataset.csv')

# --- CALCULATIONS ---
price_level_counts = restaurant_data['Price range'].value_counts().sort_index()

total_entries = len(restaurant_data)
price_ratios = (price_level_counts / total_entries) * 100

print("--- Breakdown by Price Range ---")
for price_lv, percent in price_ratios.items():
    print(f"Level {price_lv}: {percent:.2f}% of the total")

# --- PLOTTING ---
plt.figure(figsize=(10, 6))

# Creating the bar plot
plot_ax = sns.barplot(
    x=price_level_counts.index, 
    y=price_level_counts.values, 
    palette='viridis', 
    edgecolor='0.2'
)

plt.title('How Restaurants are Distributed across Price Ranges', fontsize=14, weight='bold', pad=15)
plt.xlabel('Price Tier (1 = Budget, 4 = Premium)', fontsize=11)
plt.ylabel('Count of Restaurants', fontsize=11)

for idx, val in enumerate(price_level_counts):
    percentage_val = price_ratios.iloc[idx]
    plot_ax.text(
        idx, val + 60, 
        f'{val}\n({percentage_val:.1f}%)', 
        ha='center', 
        va='bottom', 
        fontweight='semibold'
    )

plt.tight_layout()
plt.show()