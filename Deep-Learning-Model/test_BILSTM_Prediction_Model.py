import unittest
import pandas as pd
import numpy as np
from BILSTM_Prediction_Model import preprocess_data, filter_top_companies, create_dataset

class TestBILSTMPredictionModel(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2020', periods=100),
            'Close': np.random.rand(100) * 100,
            'Volume': np.random.randint(1, 1000, 100),
            'Company': ['CompanyA'] * 50 + ['CompanyB'] * 50
        })

    def test_preprocess_data(self):
        processed_data = preprocess_data(self.data.copy())
        self.assertFalse(processed_data['Close'].isnull().any(), "Close column should not have null values")
        self.assertFalse(processed_data['Volume'].isnull().any(), "Volume column should not have null values")
        self.assertFalse(processed_data['Date'].isnull().any(), "Date column should not have null values")
        self.assertFalse(processed_data['Company'].isnull().any(), "Company column should not have null values")

    def test_filter_top_companies(self):
        filtered_data = filter_top_companies(self.data.copy(), top_n=1)
        self.assertEqual(filtered_data['Company'].nunique(), 1, "There should be only one company in the filtered data")

    def test_create_dataset(self):
        look_back = 10
        scaled_data = np.random.rand(100, 1)
        X, Y = create_dataset(scaled_data, look_back)
        self.assertEqual(X.shape[0], len(scaled_data) - look_back - 1, "X should have the correct number of samples")
        self.assertEqual(X.shape[1], look_back, "X should have the correct look_back length")
        self.assertEqual(Y.shape[0], len(scaled_data) - look_back - 1, "Y should have the correct number of samples")

if __name__ == '__main__':
    unittest.main()
