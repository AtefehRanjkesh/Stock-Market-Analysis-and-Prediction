# Comprehensive Stock Market Analysis and Prediction Project

This project encompasses three interconnected subprojects aimed at providing comprehensive insights into stock market trends, analysis, and prediction using data science techniques. The three subprojects are:

1. **Bidirectional LSTM Stock Price Prediction Model**
2. **Stock Market Data Analysis**
3. **Tableau Stock Analysis**

---

## Project Overview

The goal of this project is to analyze stock market data, visualize trends, and predict future stock prices using advanced machine learning and visualization tools. It is a complete suite for financial data analysis, combining in-depth exploratory data analysis, predictive modeling, and interactive visualizations.

---

## Subprojects

### 1. Bidirectional LSTM Stock Price Prediction Model

This subproject uses a Bidirectional Long Short-Term Memory (LSTM) neural network to predict stock prices based on historical data. It employs TensorFlow for building and training the model.

#### Features:
- Predicts stock prices using historical data.
- Visualizes predictions with detailed plots.
- Includes logging for execution monitoring.
- Contains unit tests for key functions.

#### Key Files:
- `BILSTM_Prediction_Model.py`: Main script for model training and prediction.
- `test_BILSTM_Prediction_Model.py`: Unit tests for the model.
- `requirements.txt`: List of dependencies.

#### Directory Structure:
```
Deep-Learning-Model/
├── BILSTM_Prediction_Model.py
├── test_BILSTM_Prediction_Model.py
├── requirements.txt
└── README.md
```

---

### 2. Stock Market Data Analysis

This subproject performs exploratory data analysis on stock market data for the top 500 companies by market capitalization. It leverages Python libraries like Pandas, NumPy, and Matplotlib for data manipulation and visualization.

#### Features:
- Analyzes historical trends, volatility, and sector performance.
- Includes moving average analysis and correlation studies.
- Processes raw data into a clean, analysis-ready format.

#### Key Files:
- `stock_analysis.py`: Main script for analysis and visualization.
- `processed_stock_data.csv`: Processed data used for visualization and modeling.
- `requirements.txt`: List of dependencies.

#### Directory Structure:
```
Stock-Market-Analysis/
├── Data/
├── stock_analysis.py
├── processed_stock_data.csv
├── tests/
│   └── test_stock_analysis.py
└── README.md
```

---

### 3. Tableau Stock Analysis

This subproject uses Tableau to create interactive dashboards and visualizations based on processed stock data. The dashboards provide insights into stock performance, trends, and other key metrics.

#### Features:
- Interactive dashboards for stock analysis.
- Worksheets for trend analysis, volatility, and performance metrics.
- Visualizes the impact of dividends, stock splits, and moving averages.

#### Key Files:
- `Stock_Analysis.twb`: Tableau workbook containing all dashboards and analyses.
- `processed_stock_data.csv`: Data source for Tableau.

#### Directory Structure:
```
Tableau-Stock-Analysis/
├── Stock_Analysis.twb
└── processed_stock_data.csv
```

---

## Dataset Information

The dataset used in this project is:
- **Massive Yahoo Finance Dataset**
- **Yahoo Finance Dataset: Historical Stock Market Information of Top 500 Companies**

You can obtain the dataset from [Kaggle](https://www.kaggle.com/datasets/iveeaten3223times/massive-yahoo-finance-dataset) and place it in the appropriate directories before running the scripts. Please note that the dataset itself is not included in this repository and needs to be downloaded separately.

---

## Installation

### Prerequisites
- Python 3.6 or higher
- Tableau Desktop
- Required Python libraries listed in the `requirements.txt` files for each subproject.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-market-project.git
   ```
2. Install dependencies for each subproject:
   ```bash
   cd Deep-Learning-Model
   pip install -r requirements.txt

   cd ../Stock-Market-Analysis
   pip install -r requirements.txt
   ```
3. Open the Tableau workbook:
   ```
   Tableau-Stock-Analysis/Stock_Analysis.twb
   ```

---

## Usage

### Running the LSTM Model
1. Download the dataset from Kaggle and place it in the `../Data/` directory.
2. Execute the prediction model:
   ```bash
   python BILSTM_Prediction_Model.py
   ```
3. View the results in the `plots/` directory.

### Performing Stock Analysis
1. Run the analysis script:
   ```bash
   python stock_analysis.py
   ```
2. Generated plots and processed data will be saved in the respective directories.

### Tableau Analysis
1. Open `Stock_Analysis.twb` in Tableau Desktop.
2. Interact with the dashboards and worksheets for insights.

---

## Project Directory Structure
```
stock-market-project/
├── Data/
├── Deep-Learning-Model/
│   ├── BILSTM_Prediction_Model.py
│   ├── test_BILSTM_Prediction_Model.py
│   ├── requirements.txt
│   └── README.md
├── Stock-Market-Analysis/
│   ├── stock_analysis.py
│   ├── processed_stock_data.csv
│   ├── tests/
│   │   └── test_stock_analysis.py
│   └── README.md
├── Tableau-Stock-Analysis/
│   ├── Stock_Analysis.twb
│   └── processed_stock_data.csv
└── README.md (this file)
```

---


## License

This project is licensed under the MIT License.

---

## Contact

For any questions or inquiries, please contact [Atefeh Ranjkesh](mailto:at.ranjkesh@yahoo.com).

