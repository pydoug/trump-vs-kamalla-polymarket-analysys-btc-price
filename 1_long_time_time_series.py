# Overlaid Time Series Plots

import pandas as pd
import matplotlib.pyplot as plt

# File paths
bitcoin_path = r'C:/Users/Douglas/Desktop/post/bitcoin_2024-01-04_2024-11-03.csv'
odds_path = r'C:/Users/Douglas/Desktop/post/polymarket-price-data-04-01-2024-03-11-2024-1730603524427.csv'
images_path = r'C:/Users/Douglas/Desktop/post/images'

# Load data with proper date parsing
bitcoin_df = pd.read_csv(bitcoin_path, parse_dates=['Start'])
odds_df = pd.read_csv(odds_path)

# Convert 'Date (UTC)' to datetime
odds_df['Date (UTC)'] = pd.to_datetime(odds_df['Date (UTC)'], format='%m-%d-%Y %H:%M')

# Prepare data
bitcoin_df['Date'] = bitcoin_df['Start'].dt.date
odds_df['Date'] = odds_df['Date (UTC)'].dt.date

merged_df = pd.merge(bitcoin_df, odds_df, on='Date', how='inner')

# Convert probabilities to numeric and handle errors
for col in ['Donald Trump', 'Kamala Harris', 'Joe Biden']:
    merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')

# Filter data from June 2024 onwards
merged_df = merged_df[merged_df['Date'] >= pd.to_datetime('2024-06-01').date()]

# Plot
fig, ax1 = plt.subplots(figsize=(14, 7))
ax1.plot(merged_df['Date'], merged_df['Close'], color='blue', label='Bitcoin Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Bitcoin Price (USD)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(merged_df['Date'], merged_df['Donald Trump'] * 100, color='red', linestyle='--', label='Donald Trump')
ax2.set_ylabel('Probability (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.suptitle('Bitcoin Price and Donald Trump Probability (2024)')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig(f'{images_path}/bitcoin_trump_time_series.png')
plt.show()