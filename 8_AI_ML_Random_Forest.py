import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

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

# Merge data
merged_df = pd.merge(odds_df, bitcoin_df[['Date', 'Close']], on='Date', how='inner')

# date (e.g., '2024-11-03')
merged_df = merged_df[merged_df['Date'] <= '2024-11-03']


X_trump = merged_df[['Donald Trump']].values
X_kamala = merged_df[['Kamala Harris']].values
y = merged_df['Close'].values


X_train_trump, X_test_trump, y_train, y_test = train_test_split(X_trump, y, test_size=0.2, random_state=42)
X_train_kamala, X_test_kamala, _, _ = train_test_split(X_kamala, y, test_size=0.2, random_state=42)


rf_model_trump = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model_trump.fit(X_train_trump, y_train)


rf_model_kamala = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model_kamala.fit(X_train_kamala, y_train)


future_dates = pd.date_range(start='2024-11-04', end='2024-12-31')


future_odds_trump = np.full(len(future_dates), X_trump[-1][0]) + np.random.normal(0, 5, len(future_dates))
future_odds_kamala = np.full(len(future_dates), X_kamala[-1][0]) + np.random.normal(0, 5, len(future_dates))


future_pred_trump_rf = rf_model_trump.predict(future_odds_trump.reshape(-1, 1))


future_pred_kamala_rf = rf_model_kamala.predict(future_odds_kamala.reshape(-1, 1))


future_pred_trump_rf = future_pred_trump_rf * (1 + future_odds_trump * 0.007) + np.random.normal(0, 500, len(future_pred_trump_rf)) 
future_pred_kamala_rf = future_pred_kamala_rf * (1 - future_odds_kamala * 0.007) + np.random.normal(0, 500, len(future_pred_kamala_rf)) 
plt.figure(figsize=(12, 6))
plt.plot(merged_df['Date'], merged_df['Close'], label='Historical BTC Price', color='blue')
plt.plot(future_dates, future_pred_trump_rf, label='Predicted BTC Price if Trump Wins (RF)', color='green', linestyle='--')
plt.fill_between(future_dates, future_pred_trump_rf - 1000, future_pred_trump_rf + 1000, color='green', alpha=0.1)
plt.title('Bitcoin Price Predictions if Trump Wins (Random Forest)')
plt.xlabel('Date')
plt.ylabel('Bitcoin Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{images_path}/btc_price_predictions_trump_rf.png", dpi=300, bbox_inches='tight')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(merged_df['Date'], merged_df['Close'], label='Historical BTC Price', color='blue')
plt.plot(future_dates, future_pred_kamala_rf, label='Predicted BTC Price if Kamala Wins (RF)', color='red', linestyle='--')
plt.fill_between(future_dates, future_pred_kamala_rf - 1000, future_pred_kamala_rf + 1000, color='red', alpha=0.1)
plt.title('Bitcoin Price Predictions if Kamala Wins (Random Forest)')
plt.xlabel('Date')
plt.ylabel('Bitcoin Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{images_path}/btc_price_predictions_kamala_rf.png", dpi=300, bbox_inches='tight')
plt.show()
