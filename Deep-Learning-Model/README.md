# Bidirectional LSTM Stock Price Prediction Model

This project uses a Bidirectional LSTM model to predict stock prices based on historical data.

## Requirements

Ensure you have the following packages installed:

```
pandas==1.5.3
matplotlib==3.6.2
numpy==1.23.4
scikit-learn==1.1.3
tensorflow==2.10.0
```

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/finance-data-science-portfolio.git
    cd finance-data-science-portfolio/Deep-Learning-Model
    ```

2. **Prepare the data:**

    Ensure you have the dataset file `stock_details_5_years.csv` in the `../Data/` directory.

3. **Run the model:**

    Execute the following command to run the Bidirectional LSTM prediction model:

    ```bash
    python BILSTM_Prediction_Model.py
    ```

4. **View the results:**

    The predicted stock prices will be plotted and saved in the `plots` directory as `stock_price_prediction.png`.

## Logging

The script uses logging to provide detailed information about the execution flow. Logs are printed to the console with timestamps and log levels.

## Unit Tests

Unit tests are provided to ensure the correctness of the key functions. To run the tests, execute the following command:

```bash
python -m unittest test_BILSTM_Prediction_Model.py
```

## Directory Structure

```
finance-data-science-portfolio/
├── Data/
│   └── stock_details_5_years.csv
├── Deep-Learning-Model/
│   ├── BILSTM_Prediction_Model.py
│   ├── test_BILSTM_Prediction_Model.py
│   ├── requirements.txt
│   └── README.md
└── plots/
    └── stock_price_prediction.png
```

## License

This project is licensed under the MIT License.