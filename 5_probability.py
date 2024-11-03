import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

odds_path = r'C:/Users/Douglas/Desktop/post/polymarket-price-data-04-01-2024-03-11-2024-1730603524427.csv'
bitcoin_path = r'C:/Users/Douglas/Desktop/post/bitcoin_2024-01-04_2024-11-03.csv'
images_path = r'C:/Users/Douglas/Desktop/post/images'

odds_df = pd.read_csv(odds_path)
bitcoin_df = pd.read_csv(bitcoin_path)

odds_df['Date'] = pd.to_datetime(odds_df['Date (UTC)'], format='%m-%d-%Y %H:%M')
bitcoin_df['Date'] = pd.to_datetime(bitcoin_df['Start'])

for col in ['Donald Trump', 'Kamala Harris']:
    odds_df[col] = pd.to_numeric(odds_df[col], errors='coerce') * 100

odds_df = odds_df.dropna(subset=['Donald Trump', 'Kamala Harris'])

merged_df = pd.merge(odds_df, bitcoin_df[['Date', 'Close']], on='Date', how='inner')

merged_df = merged_df[merged_df['Date'] >= '2024-07-01']

plt.figure(figsize=(10, 7))
plt.scatter(merged_df['Close'], merged_df['Donald Trump'], alpha=0.6, color='blue', edgecolor='k', s=60)
plt.title('Bitcoin Price vs Donald Trump Probability', fontsize=16)
plt.xlabel('Bitcoin Price', fontsize=14)
plt.ylabel('Donald Trump Probability (%)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

z_trump = np.polyfit(merged_df['Close'], merged_df['Donald Trump'], 1)
p_trump = np.poly1d(z_trump)
plt.plot(merged_df['Close'], p_trump(merged_df['Close']), color='red', linestyle='-', linewidth=2, label='Trend Line')
plt.legend(fontsize=12)

corr_trump = merged_df['Close'].corr(merged_df['Donald Trump'])
plt.text(0.05, 0.95, f'Correlation: {corr_trump:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig(f'{images_path}/scatter_trump_bitcoin_price.png', dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 7))
plt.scatter(merged_df['Close'], merged_df['Kamala Harris'], alpha=0.6, color='green', edgecolor='k', s=60)
plt.title('Bitcoin Price vs Kamala Harris Probability', fontsize=16)
plt.xlabel('Bitcoin Price', fontsize=14)
plt.ylabel('Kamala Harris Probability (%)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

z_harris = np.polyfit(merged_df['Close'], merged_df['Kamala Harris'], 1)
p_harris = np.poly1d(z_harris)
plt.plot(merged_df['Close'], p_harris(merged_df['Close']), color='red', linestyle='-', linewidth=2, label='Trend Line')
plt.legend(fontsize=12)

corr_harris = merged_df['Close'].corr(merged_df['Kamala Harris'])
plt.text(0.05, 0.95, f'Correlation: {corr_harris:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig(f'{images_path}/scatter_kamala_bitcoin_price.png', dpi=300, bbox_inches='tight')
plt.show()
