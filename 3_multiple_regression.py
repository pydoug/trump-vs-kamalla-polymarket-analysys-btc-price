# Multiple Linear Regression Analysis with Additional Variables

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# File paths
bitcoin_path = r'C:/Users/Douglas/Desktop/post/bitcoin_2024-01-04_2024-11-03.csv'
odds_path = r'C:/Users/Douglas/Desktop/post/polymarket-price-data-04-01-2024-03-11-2024-1730603524427.csv'
images_path = r'C:/Users/Douglas/Desktop/post/images'

# Load data
bitcoin_df = pd.read_csv(bitcoin_path, parse_dates=['Start'])
odds_df = pd.read_csv(odds_path)


odds_df['Date (UTC)'] = pd.to_datetime(odds_df['Date (UTC)'], format='%m-%d-%Y %H:%M')


bitcoin_df['Date'] = bitcoin_df['Start'].dt.date
odds_df['Date'] = odds_df['Date (UTC)'].dt.date

merged_df = pd.merge(bitcoin_df, odds_df, on='Date', how='inner')


merged_df['Donald Trump'] = pd.to_numeric(merged_df['Donald Trump'], errors='coerce')


merged_df = merged_df.dropna(subset=['Donald Trump', 'Close'])

X = merged_df[['Donald Trump']]
y = merged_df['Close']
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())


with open(f'{images_path}/multiple_regression_summary.txt', 'w') as f:
    f.write(model.summary().as_text())

plt.figure(figsize=(10, 6))


scatter = plt.scatter(merged_df['Donald Trump'], merged_df['Close'], c=merged_df['Donald Trump'], cmap='plasma', alpha=0.6, edgecolor='w', linewidth=0.5)


cbar = plt.colorbar(scatter)
cbar.set_label('Donald Trump Probability')


sns.regplot(x=merged_df['Donald Trump'], y=merged_df['Close'], scatter=False, line_kws={'color': 'red', 'linewidth': 2}, lowess=True)

plt.xlabel('Donald Trump Probability')
plt.ylabel('Bitcoin Price (USD)')
plt.title('Bitcoin Price vs. Donald Trump Probability')


plt.savefig(f'{images_path}/improved_multiple_regression_visualization.png', dpi=300, bbox_inches='tight')
plt.show()
