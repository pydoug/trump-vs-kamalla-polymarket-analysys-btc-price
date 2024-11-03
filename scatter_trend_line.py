# Scatter Plot with Trend Line

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bitcoin_path = r'C:/Users/Douglas/Desktop/post/bitcoin_2024-01-04_2024-11-03.csv'
odds_path = r'C:/Users/Douglas/Desktop/post/polymarket-price-data-04-01-2024-03-11-2024-1730603524427.csv'
images_path = r'C:/Users/Douglas/Desktop/post/images'

bitcoin_df = pd.read_csv(bitcoin_path)
odds_df = pd.read_csv(odds_path)

bitcoin_df['Date'] = pd.to_datetime(bitcoin_df['Start']).dt.date
odds_df['Date'] = pd.to_datetime(odds_df['Date (UTC)']).dt.date

merged_df = pd.merge(bitcoin_df, odds_df, on='Date', how='inner')

merged_df['Donald Trump'] = merged_df['Donald Trump'].astype(float)
plt.figure(figsize=(10,6))
scatter = plt.scatter(merged_df['Donald Trump'], merged_df['Close'], c=merged_df['Kamala Harris'], cmap='viridis', alpha=0.5)
plt.colorbar(scatter, label='Kamala Harris Probability')
sns.regplot(x=merged_df['Donald Trump'], y=merged_df['Close'], scatter=False, line_kws={'color':'red'})
plt.xlabel('Donald Trump Probability')
plt.ylabel('Bitcoin Price (USD)')
plt.title('Bitcoin Price vs. Donald Trump Probability with Kamala Harris Influence')
plt.savefig(f'{images_path}/scatter_trump_bitcoin_enhanced.png')
plt.show()
