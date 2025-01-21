import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import logging

# Constants
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PLOTS_DIR = os.path.join(SCRIPT_DIR, 'plots')
DATA_PATH = os.path.join(SCRIPT_DIR, '../Data/stock_details_5_years.csv')
PROCESSED_DATA_PATH = os.path.join(SCRIPT_DIR, 'processed_stock_data.csv')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a directory to save plots
if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)
    logging.info(f"Created directory: {PLOTS_DIR}")

# Load the dataset with error handling
def load_data(path):
    try:
        data = pd.read_csv(path)
        if data.empty:
            raise ValueError("The dataset is empty.")
        logging.info(f"Loaded data from {path}")
        return data
    except FileNotFoundError:
        logging.error(f"Error: The dataset file at {path} was not found.")
        exit()
    except ValueError as e:
        logging.error(f"Error: {e}")
        exit()

data = load_data(DATA_PATH)

# Preprocessing: Handle missing values and parse dates
def preprocess_data(data):
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.sort_values('Date')
    data['Close'] = data['Close'].fillna(method='ffill')
    data['Volume'] = data['Volume'].fillna(0)
    data = data.dropna(subset=['Company'])
    logging.info("Preprocessed data")
    return data

data = preprocess_data(data)

# Filter out top 10 companies
def get_top_companies(data, n=10):
    top_companies = data['Company'].value_counts().head(n).index
    logging.info(f"Filtered top {n} companies")
    return top_companies

top_companies = get_top_companies(data)
trend_data = data[data['Company'].isin(top_companies)]

# Calculate daily percentage change
trend_data['Daily_Change'] = trend_data.groupby('Company')['Close'].pct_change() * 100
trend_data['Daily_Change'] = trend_data['Daily_Change'].fillna(0)

# Calculate rolling volatility and moving averages
def calculate_rolling_metrics(df, window, column, metric='std'):
    if metric == 'std':
        return df.groupby('Company')[column].rolling(window=window).std().reset_index(level=0, drop=True)
    elif metric == 'mean':
        return df.groupby('Company')[column].rolling(window=window).mean().reset_index(level=0, drop=True)

trend_data['Volatility'] = calculate_rolling_metrics(trend_data, 30, 'Daily_Change')
trend_data['Volatility'] = trend_data.groupby('Company')['Volatility'].fillna(method='bfill').fillna(method='ffill')

trend_data['MA50'] = calculate_rolling_metrics(trend_data, 50, 'Close', metric='mean')
trend_data['MA50'] = trend_data.groupby('Company')['MA50'].fillna(method='bfill').fillna(method='ffill')

trend_data['MA200'] = calculate_rolling_metrics(trend_data, 200, 'Close', metric='mean')
trend_data['MA200'] = trend_data.groupby('Company')['MA200'].fillna(method='bfill').fillna(method='ffill')

# Export processed data
trend_data.to_csv(PROCESSED_DATA_PATH, index=False)
logging.info(f"Processed data saved to '{PROCESSED_DATA_PATH}'")

# Function to save plots
def save_plot(fig, filename):
    fig.savefig(os.path.join(PLOTS_DIR, filename))
    plt.close(fig)
    logging.info(f"Saved plot: {filename}")

# Goal 1: Trend Analysis (Multiple Plots)
def plot_trends(companies, data):
    plt.figure(figsize=(14, 7))
    for company in companies:
        company_data = data[data['Company'] == company]
        plt.plot(company_data['Date'], company_data['Close'], label=company)
    plt.title('Stock Price Trends of Top 10 Companies')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    save_plot(plt.gcf(), 'trend_analysis.png')

plot_trends(top_companies, trend_data)

# Distribution of Closing Prices
plt.figure(figsize=(12, 6))
sns.histplot(data['Close'], bins=50, kde=True)
plt.title('Distribution of Closing Prices')
plt.xlabel('Close Price')
plt.ylabel('Frequency')
save_plot(plt.gcf(), 'distribution_of_closing_prices.png')

# Line Plot of Closing Prices for a single company (example: first company)
def plot_single_company_trend(company, data):
    single_company_data = data[data['Company'] == company]
    plt.figure(figsize=(14, 7))
    plt.plot(single_company_data['Date'], single_company_data['Close'])
    plt.title(f'{company} Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    save_plot(plt.gcf(), f'{company}_trend.png')

plot_single_company_trend(top_companies[0], trend_data)

# Goal 2: Volatility Assessment (Multiple Plots)
# Box plot for daily percentage changes
plt.figure(figsize=(14, 7))
sns.boxplot(x='Company', y='Daily_Change', data=trend_data)
plt.title('Daily Percentage Change by Company')
plt.ylabel('Percentage Change')
save_plot(plt.gcf(), 'volatility_boxplot.png')

# Rolling Standard Deviation (Volatility)
def plot_rolling_volatility(companies, data, window=30):
    plt.figure(figsize=(14, 7))
    for company in companies:
        company_data = data[data['Company'] == company]
        plt.plot(company_data['Date'], company_data['Volatility'], label=company)
    plt.title(f'Volatility Analysis (Rolling {window}-Day Std Dev)')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    save_plot(plt.gcf(), 'rolling_volatility_analysis.png')

plot_rolling_volatility(top_companies, trend_data)

# Goal 3: Sector/Company Performance (Multiple Plots)
# Average Closing Price by Company
def plot_avg_closing_price(data):
    avg_close = data.groupby('Company')['Close'].mean().reset_index()
    avg_close = avg_close.sort_values(by='Close', ascending=False)
    plt.figure(figsize=(14, 7))
    sns.barplot(x='Close', y='Company', data=avg_close)
    plt.title('Average Closing Price by Top Companies')
    plt.xlabel('Average Closing Price')
    save_plot(plt.gcf(), 'company_performance.png')

plot_avg_closing_price(trend_data)

# Performance over time for each company
def plot_performance_over_time(companies, data):
    plt.figure(figsize=(14, 7))
    for company in companies:
        company_data = data[data['Company'] == company]
        plt.plot(company_data['Date'], company_data['Close'], label=company)
    plt.title('Performance of Top Companies Over Time')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    save_plot(plt.gcf(), 'performance_over_time.png')

plot_performance_over_time(top_companies, trend_data)

# Goal 4: Correlation Analysis (Multiple Plots)
# Pair plot to show relationships between stock metrics
plt.figure(figsize=(12, 10))
sns.pairplot(trend_data[['Open', 'High', 'Low', 'Close', 'Volume']])
plt.suptitle('Pair Plot of Stock Metrics', y=1.02)
save_plot(plt.gcf(), 'pair_plot_stock_metrics.png')

# Scatter plot for Close vs Volume
plt.figure(figsize=(14, 7))
sns.scatterplot(x='Volume', y='Close', data=trend_data)
plt.title('Scatter Plot of Close vs Volume')
plt.xlabel('Volume')
plt.ylabel('Closing Price')
save_plot(plt.gcf(), 'close_vs_volume.png')

# Goal 5: Dividend and Stock Split Impact (Multiple Plots)
# Box plot of Closing Prices by Company
plt.figure(figsize=(14, 7))
sns.boxplot(x='Company', y='Close', data=trend_data)
plt.title('Box Plot of Closing Prices by Company')
plt.xlabel('Company')
plt.ylabel('Closing Price')
save_plot(plt.gcf(), 'box_plot_closing_prices.png')

# Line plot of Average Closing Prices Over Time
def plot_avg_closing_prices_over_time(companies, data):
    avg_close_over_time = data.groupby(['Date', 'Company'])['Close'].mean().reset_index()
    plt.figure(figsize=(14, 7))
    for company in companies:
        company_data = avg_close_over_time[avg_close_over_time['Company'] == company]
        plt.plot(company_data['Date'], company_data['Close'], label=company)
    plt.title('Average Closing Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Closing Price')
    plt.legend()
    save_plot(plt.gcf(), 'avg_closing_prices_over_time.png')

plot_avg_closing_prices_over_time(top_companies, trend_data)

# Goal 6: Moving Averages (Multiple Plots)
def plot_moving_averages(companies, data):
    plt.figure(figsize=(14, 7))
    for company in companies:
        company_data = data[data['Company'] == company]
        plt.plot(company_data['Date'], company_data['Close'], label=f'{company} Close')
        plt.plot(company_data['Date'], company_data['MA50'], label=f'{company} MA50')
        plt.plot(company_data['Date'], company_data['MA200'], label=f'{company} MA200')
    plt.title('Moving Averages (MA50 and MA200)')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    save_plot(plt.gcf(), 'moving_averages.png')

plot_moving_averages(top_companies, trend_data)

logging.info("Analysis and plots completed. Check the saved images and processed data.")