# Pearson Correlation Calculation

import pandas as pd

bitcoin_path = r'C:/Users/Douglas/Desktop/post/bitcoin_2024-01-04_2024-11-03.csv'
odds_path = r'C:/Users/Douglas/Desktop/post/polymarket-price-data-04-01-2024-03-11-2024-1730603524427.csv'

bitcoin_df = pd.read_csv(bitcoin_path)
odds_df = pd.read_csv(odds_path)

bitcoin_df['Date'] = pd.to_datetime(bitcoin_df['Start']).dt.date
odds_df['Date'] = pd.to_datetime(odds_df['Date (UTC)']).dt.date

merged_df = pd.merge(bitcoin_df, odds_df, on='Date', how='inner')

for col in ['Donald Trump', 'Kamala Harris', 'Joe Biden']:
    merged_df[col] = merged_df[col].astype(float)

correlation_matrix = merged_df[['Close', 'Donald Trump', 'Kamala Harris', 'Joe Biden']].corr()
print(correlation_matrix)

images_path = r'C:/Users/Douglas/Desktop/post/images'
correlation_matrix.to_csv(f'{images_path}/correlation_matrix.csv')
