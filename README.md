# Polymarket Analysis - BTC Price in Elections

This repository contains an analysis of Polymarket data focusing on Bitcoin price movements in response to political events, specifically the Trump vs. Kamala election prediction market. The study aims to understand how political sentiment and key election-related events influence BTC price volatility.

## Project Overview

This project was created to explore the relationship between political events and cryptocurrency markets, with a specific focus on:

- **Market Sentiment**: How political events impact market sentiment.
- **Price Correlation**: Analyzing if certain events lead to notable changes in BTC price.
- **Polymarket Data**: Using data from Polymarket, a decentralized information market platform, to conduct the analysis.

**Analysis Breakdown**

**Long-Term Time Series Analysis (1_long_time_time_series.py)**
📈 Description: This script performs a time series analysis over a long period, identifying trends, patterns, and seasonality within the data.

**Linear Regression (2_linear_regression.py)**
🔹 Description: Implements a linear regression model to determine the linear relationship between a dependent variable and one or more independent variables.

**Multiple Regression (3_multiple_regression.py)**
🔹 Description: A multiple regression analysis that incorporates multiple independent variables to predict the outcome of a dependent variable, providing insights into complex relationships.

**Stacked Area Chart (4_stack_area.py)**
📊 Description: This script generates a stacked area chart, useful for visualizing the cumulative contribution of multiple data series over time.

**Probability Analysis (5_probability.py)**
🔹 Description: Conducts a probability analysis, likely exploring probability distributions, conditional probabilities, or likelihood of events within the dataset.

**Polynomial Regression (6_polynomial_regression.py)**
🔹 Description: Applies polynomial regression to model the relationship between variables in a nonlinear manner, capturing more complex patterns than linear regression.

**Logarithmic Regression (7_logarithmic_regression.py)**
🔹 Description: This script uses logarithmic regression to explore relationships where the rate of change is not constant, often applicable to data with rapid growth that slows over time.

**AI/ML Random Forest Model (8_AI_ML_Random_Forest.py)**
🌲 Description: Implements a Random Forest model, a machine learning algorithm that utilizes multiple decision trees to improve prediction accuracy and reduce overfitting.

**And many others**

## Project Structure
- /data: Contains the raw and processed data.
- /images: Folder to store generated charts and visualizations.

## Data Sources

The analysis uses data sourced from:
- **Polymarket**: Historical event data for the election predictions.
- https://polymarket.com/event/presidential-election-winner-2024?tid=1730652082325
  
- **Cryptocurrency Exchange**: BTC price history from various exchanges to compare with Polymarket events.
- https://coincodex.com/crypto/bitcoin/historical-data/

## Installation & Setup

To run the analysis, you will need to clone the repository and install the required dependencies.

## Clone the Repository

```
git clone https://github.com/pydoug/trump-vs-kamalla-polymarket-analysys-btc-price
cd trump-vs-kamalla-polymarket-analysys-btc-price
```
### Install Dependencies
Ensure you have Python installed. Then, use the following command to install the required libraries:
```
pip install -r requirements.txt
```


