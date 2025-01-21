import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import logging
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Bidirectional
import tensorflow as tf

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure TensorFlow to use the GPU if available
try:
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logging.info("GPU is available and configured.")
    else:
        logging.warning("GPU is not available. Using CPU.")
except RuntimeError as e:
    logging.error(f"Error configuring GPU: {e}")

def create_plots_directory(directory='plots'):
    """Create a directory to save plots if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")

def load_dataset(filepath):
    """Load the dataset with error handling."""
    if not os.path.exists(filepath):
        logging.error("Error: The dataset file was not found.")
        exit()
    data = pd.read_csv(filepath)
    logging.info(f"Dataset loaded successfully from {filepath}")
    return data

def preprocess_data(data):
    """Preprocess the data: handle missing values and parse dates."""
    logging.info("Preprocessing data...")
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.sort_values('Date')
    data['Close'] = data['Close'].fillna(method='ffill')
    data['Volume'] = data['Volume'].fillna(0)
    data = data.dropna(subset=['Company'])
    logging.info("Data preprocessing completed.")
    return data

def filter_top_companies(data, top_n=10):
    """Filter out the top N companies based on the number of records."""
    logging.info(f"Filtering top {top_n} companies...")
    top_companies = data['Company'].value_counts().head(top_n).index
    filtered_data = data[data['Company'].isin(top_companies)]
    logging.info("Top companies filtered.")
    return filtered_data

def create_dataset(dataset, look_back=60):
    """Create a dataset with look_back."""
    logging.info(f"Creating dataset with look_back={look_back}...")
    X, Y = [], []
    for i in range(len(dataset) - look_back):
        X.append(dataset[i:i + look_back, 0])
        Y.append(dataset[i + look_back, 0])
    logging.info("Dataset creation completed.")
    return np.array(X), np.array(Y)

def build_bidirectional_lstm_model(input_shape):
    """Build and compile the Bidirectional LSTM model."""
    logging.info("Building Bidirectional LSTM model...")
    model = Sequential([
        Bidirectional(LSTM(50, return_sequences=True), input_shape=input_shape),
        Bidirectional(LSTM(50)),
        Dense(1)
    ])
    model.compile(loss='mean_squared_error', optimizer='adam')
    logging.info("Model built and compiled.")
    return model

def plot_predictions(dates, actual, train_predict, test_predict, look_back):
    """Plot the actual and predicted stock prices."""
    logging.info("Plotting predictions...")
    plt.figure(figsize=(12, 6))

    # Plot actual stock prices
    plt.plot(dates[:len(actual)], actual, label='Actual Stock Price', color='blue')

    # Plot train predictions
    train_dates = dates[look_back:look_back + len(train_predict)]
    plt.plot(train_dates, train_predict, label='Train Predict', color='green')

    # Plot test predictions
    test_start_index = look_back + len(train_predict)
    test_dates = dates[test_start_index:test_start_index + len(test_predict)]
    plt.plot(test_dates, test_predict, label='Test Predict', color='red')

    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('Stock Price Prediction')
    plt.legend()
    plt.savefig('plots/stock_price_prediction.png')
    plt.show()
    logging.info("Predictions plotted and saved.")

def main():
    logging.info("Starting main process...")
    create_plots_directory()

    data = load_dataset('../Data/stock_details_5_years.csv')
    data = preprocess_data(data)

    if data.empty:
        logging.error("Error: The dataset is empty.")
        exit()

    trend_data = filter_top_companies(data)
    company_data = trend_data[trend_data['Company'] == trend_data['Company'].value_counts().index[0]]

    # Scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(company_data['Close'].values.reshape(-1, 1))

    # Create datasets
    look_back = 60
    X, Y = create_dataset(scaled_data, look_back)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Split into training and testing datasets
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    Y_train, Y_test = Y[:train_size], Y[train_size:]

    # Build and train the model
    model = build_bidirectional_lstm_model((look_back, 1))
    model.fit(X_train, Y_train, epochs=20, batch_size=1, verbose=2)

    # Make predictions
    train_predict = scaler.inverse_transform(model.predict(X_train)).reshape(-1)
    test_predict = scaler.inverse_transform(model.predict(X_test)).reshape(-1)

    # Plot predictions
    plot_predictions(
        dates=company_data['Date'].values, 
        actual=company_data['Close'].values, 
        train_predict=train_predict, 
        test_predict=test_predict, 
        look_back=look_back
    )
    logging.info("Main process completed.")

if __name__ == "__main__":
    main()
