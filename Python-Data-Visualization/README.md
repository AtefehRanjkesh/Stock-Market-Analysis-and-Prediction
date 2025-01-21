# Stock Market Data Analysis

This project analyzes stock market data from Yahoo Finance using various Python libraries to visualize and understand different aspects of the data.

## Project Overview

This project aims to provide a comprehensive analysis of stock market data for the top 500 companies by market capitalization over the last five years. The analysis includes trend analysis, volatility assessment, sector/company performance, correlation analysis, and the impact of dividends and stock splits.

## Goals

1. **Trend Analysis**: Understand the historical price trends of selected stocks and compare their performance.
2. **Volatility Assessment**: Investigate the trading volume trends over time and identify any significant changes.
3. **Sector/Company Performance**: Examine the performance of different companies and sectors.
4. **Correlation Analysis**: Analyze the correlation between different stock metrics.
5. **Dividend and Stock Split Impact**: Assess the impact of dividends and stock splits on stock prices.
6. **Moving Averages and Trend Analysis**: Calculate and visualize moving averages to identify trends and potential buy/sell signals.

## Libraries Used

- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computing.
- **Matplotlib**: Data visualization.
- **Seaborn**: Statistical data visualization.
- **Logging**: Logging progress and errors.

## Installation

1. Ensure you have Python installed (version 3.6 or higher).
2. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/stock-market-analysis.git
   ```
3. Navigate to the project directory:
   ```sh
   cd stock-market-analysis
   ```
4. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place the dataset (`stock_details_5_years.csv`) in the `Data` directory.
2. Run the analysis script:
   ```sh
   python stock_analysis.py
   ```
3. The script will generate various plots and save them in the `plots` directory. It will also export the processed data to `processed_stock_data.csv`.

## Running Tests

To run the unit tests, use the following command:
```sh
python -m unittest discover -s tests
```

## Analysis Details

### Trend Analysis

- **Trend Analysis**: Plots the closing price trends for the top 10 companies.
- **Distribution of Closing Prices**: Shows the distribution of closing prices for all companies.
- **Single Company Trend**: Plots the closing price trend for a single company.

### Volatility Assessment

- **Daily Percentage Change**: Box plot showing the daily percentage change by company.
- **Rolling Volatility**: Plots the rolling standard deviation (volatility) for the top companies.

### Sector/Company Performance

- **Average Closing Price by Company**: Bar plot showing the average closing price for the top companies.
- **Performance Over Time**: Line plot showing the performance of top companies over time.

### Correlation Analysis

- **Pair Plot of Stock Metrics**: Pair plot showing the relationships between different stock metrics.
- **Close vs Volume Scatter Plot**: Scatter plot showing the relationship between closing price and volume.

### Dividend and Stock Split Impact

- **Box Plot of Closing Prices by Company**: Box plot showing the distribution of closing prices for each company.
- **Average Closing Prices Over Time**: Line plot showing the average closing prices of the top companies over time.

### Moving Averages

- **Moving Averages (MA50 and MA200)**: Plots the 50-day and 200-day moving averages for the top companies.

## Processed Data

The processed data differs from the original data in several ways due to the preprocessing steps applied during the analysis:

1. **Handled Missing Values**: Missing values in the 'Close' column are forward-filled, and missing values in the 'Volume' column are filled with 0. Rows with missing 'Company' values are dropped.
2. **Sorted Data**: The data is sorted by the 'Date' column to ensure chronological order.
3. **Filtered Companies**: The processed data includes only the top 10 companies by market capitalization.
4. **Additional Columns**: New columns such as 'Daily_Change', 'Volatility', 'MA50', and 'MA200' are added for analysis purposes. Null values in these columns are handled using backfill (`bfill`) followed by forward fill (`ffill`).


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.















