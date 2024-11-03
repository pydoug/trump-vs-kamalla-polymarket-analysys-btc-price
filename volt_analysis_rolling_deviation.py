# Volatility Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
bitcoin_path = r'C:/Users/Douglas/Desktop/post/bitcoin_2024-01-04_2024-11-03.csv'
odds_path = r'C:/Users/Douglas/Desktop/post/polymarket-price-data-04-01-2024-03-11-2024-1730603524427.csv'
images_path = r'C:/Users/Douglas/Desktop/post/images'

bitcoin_df = pd.read_csv(bitcoin_path)
odds_df = pd.read_csv(odds_path)


bitcoin_df['Date'] = pd.to_datetime(bitcoin_df['Start'])
odds_df['Date'] = pd.to_datetime(odds_df['Date (UTC)'])

merged_df = pd.merge(bitcoin_df, odds_df, on='Date', how='inner')

merged_df['Donald Trump'] = merged_df['Donald Trump'].astype(float)
merged_df['Returns'] = merged_df['Close'].pct_change()
window_size = 15
merged_df['Volatility'] = merged_df['Returns'].rolling(window=window_size).std() * np.sqrt(window_size)

fig, ax1 = plt.subplots(figsize=(12,6))
ax1.plot(merged_df['Date'], merged_df['Volatility'], color='blue', label='Bitcoin Volatility')
ax1.set_xlabel('Date')
ax1.set_ylabel('Volatility', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(merged_df['Date'], merged_df['Donald Trump']*100, color='red', linestyle='--', label='Donald Trump')
ax2.set_ylabel('Probability (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.suptitle('Bitcoin Volatility and Donald Trump Probability')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.savefig(f'{images_path}/volatility_vs_trump.png')
plt.show()
