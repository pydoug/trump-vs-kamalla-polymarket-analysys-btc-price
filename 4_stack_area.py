import pandas as pd
import matplotlib.pyplot as plt


odds_path = r'C:/Users/Douglas/Desktop/post/polymarket-price-data-04-01-2024-03-11-2024-1730603524427.csv'
bitcoin_path = r'C:/Users/Douglas/Desktop/post/bitcoin_2024-01-04_2024-11-03.csv'
images_path = r'C:/Users/Douglas/Desktop/post/images'


odds_df = pd.read_csv(odds_path)
bitcoin_df = pd.read_csv(bitcoin_path)


odds_df['Date'] = pd.to_datetime(odds_df['Date (UTC)'], format='%m-%d-%Y %H:%M')
bitcoin_df['Date'] = pd.to_datetime(bitcoin_df['Start'])

for col in ['Donald Trump', 'Kamala Harris', 'Joe Biden']:
    odds_df[col] = pd.to_numeric(odds_df[col], errors='coerce') * 100

odds_df = odds_df.dropna(subset=['Donald Trump', 'Kamala Harris', 'Joe Biden'])

merged_df = pd.merge(odds_df, bitcoin_df[['Date', 'Close']], on='Date', how='inner')

merged_df = merged_df[merged_df['Date'] >= '2024-07-01']

min_price = merged_df['Close'].min()
max_price = merged_df['Close'].max()
merged_df['Normalized_Close'] = 40 + (merged_df['Close'] - min_price) * (20 / (max_price - min_price))
merged_df['Normalized_Close'] = merged_df['Normalized_Close'].clip(40, 60)

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.stackplot(merged_df['Date'], 
              merged_df['Donald Trump'], 
              merged_df['Kamala Harris'], 
              merged_df['Joe Biden'], 
              labels=['Donald Trump', 'Kamala Harris', 'Joe Biden'],
              alpha=0.7)
ax1.plot(merged_df['Date'], merged_df['Normalized_Close'], color='red', linestyle='-', linewidth=1.5, alpha=0.6, label='Bitcoin Price (Soft Red)')
ax1.set_xlabel('Date')
ax1.set_ylabel('Probability (%) / Normalized Bitcoin Price')
ax1.axhline(y=50, color='black', linestyle='--', linewidth=1, label='50% Probability')
ax1.set_ylim(0, 100)
ax1.legend(loc='lower right')

plt.title("Candidates' Probabilities Over Time with Bitcoin Price")
plt.savefig(f'{images_path}/stacked_area_probabilities_with_bitcoin.png')
plt.show()