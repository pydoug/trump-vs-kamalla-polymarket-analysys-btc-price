# Multiple Linear Regression Analysis

import pandas as pd
import statsmodels.api as sm

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

# Drop rows with missing values in the relevant columns
merged_df = merged_df.dropna(subset=['Donald Trump', 'Kamala Harris', 'Joe Biden', 'Close'])

# Regression analysis
X = merged_df[['Donald Trump', 'Kamala Harris', 'Joe Biden']]
y = merged_df['Close']
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())

# Save summary
with open(f'{images_path}/regression_summary.txt', 'w') as f:
    f.write(model.summary().as_text())
