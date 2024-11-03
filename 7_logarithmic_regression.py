# Logarithmic Regression Analysis of Bitcoin Returns vs Candidate Odds

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


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


for candidate in ['Donald Trump', 'Kamala Harris']:
    X = np.log(merged_df['Close'].values).reshape(-1, 1) 
    y = merged_df[candidate].values.reshape(-1, 1)


    model = LinearRegression()
    model.fit(X, y)


    y_pred = model.predict(X)


    plt.figure(figsize=(10, 7))
    plt.scatter(merged_df['Close'], merged_df[candidate], alpha=0.5, label='Data', color='blue' if candidate == 'Donald Trump' else 'green', marker='o' if candidate == 'Donald Trump' else '^', edgecolor='w', linewidth=0.5)
    plt.plot(merged_df['Close'], y_pred, color='red', linewidth=2, label='Logarithmic Fit')
    plt.title(f'Bitcoin Price vs {candidate} Probability (Logarithmic Fit)', fontsize=16)
    plt.xlabel('Bitcoin Price', fontsize=14)
    plt.ylabel(f'{candidate} Probability (%)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{images_path}/logarithmic_regression_bitcoin_odds_{candidate.replace(' ', '_').lower()}.png", dpi=300, bbox_inches='tight')
    plt.show()
