import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
df['country'] = df['country'].fillna(df['country'].mode()[0])

# Chart 5: Netflix Content by Rating (pie)
plt.figure(figsize=(8, 8))
type_counts = df['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Netflix Content by Rating')
plt.savefig('images/chart_5.png', bbox_inches='tight')

# Chart 6: Top 10 Countries by Content Production (pie)
plt.figure(figsize=(10, 10))
top_countries = df['country'].value_counts().head(10)
plt.pie(top_countries, labels=top_countries.index, autopct='%1.1f%%')
plt.title('Top 10 Countries by Content Production')
plt.savefig('images/chart_6.png', bbox_inches='tight')

# Chart 7: Netflix Content: Movies vs TV Shows (bar)
plt.figure(figsize=(10, 8))
type_counts.plot(kind='bar', color='blue')
plt.title('Netflix Content: Movies vs TV Shows')
plt.xlabel('Content Type')
plt.ylabel('Number of Titles')
plt.xticks(rotation=0)
plt.savefig('images/chart_7.png', bbox_inches='tight')
