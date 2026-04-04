import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset.csv')

# 2. IDENTIFY RESTAURANT CHAINS
name_counts = df['Restaurant Name'].value_counts()
chains = name_counts[name_counts > 1]

# 3. ANALYZE RATINGS AND POPULARITY
df_chains = df[df['Restaurant Name'].isin(chains.index)]

# Calculate Average Rating, Total Votes (Popularity), and Outlet Count for each chain
chain_analysis = df_chains.groupby('Restaurant Name').agg({
    'Aggregate rating': 'mean',
    'Votes': 'sum',
    'Restaurant ID': 'count' # This counts the number of outlets
}).rename(columns={'Aggregate rating': 'Avg Rating', 'Votes': 'Total Votes', 'Restaurant ID': 'Outlets'})

# Sort by the number of outlets to see the biggest chains
top_chains = chain_analysis.sort_values(by='Outlets', ascending=False).head(10)

print("--- TOP 10 RESTAURANT CHAINS BY OUTLETS ---")
print(top_chains)

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

popular_chains = chain_analysis.sort_values(by='Total Votes', ascending=False).head(10)
ax = sns.barplot(x=popular_chains['Total Votes'], y=popular_chains.index, palette='flare')

plt.title('Most Popular Restaurant Chains (Based on Total Votes)', fontsize=16, fontweight='bold')
plt.xlabel('Total Votes Received', fontsize=12)
plt.ylabel('Restaurant Chain Name', fontsize=12)

plt.tight_layout()
plt.show()