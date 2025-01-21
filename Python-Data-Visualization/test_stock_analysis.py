import unittest
import pandas as pd
import os
from stock_analysis import load_data, preprocess_data, get_top_companies, calculate_rolling_metrics

class TestStockAnalysis(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2020', periods=5),
            'Company': ['A', 'B', 'A', 'B', 'A'],
            'Close': [100, 200, 110, 210, 120],
            'Volume': [1000, 2000, 1500, 2500, 1800]
        })
        # Create a sample CSV file for testing load_data
        self.sample_csv_path = 'sample_stock_data.csv'
        self.data.to_csv(self.sample_csv_path, index=False)

    def tearDown(self):
        # Remove the sample CSV file after tests
        if os.path.exists(self.sample_csv_path):
            os.remove(self.sample_csv_path)

    def test_load_data(self):
        try:
            data = load_data(self.sample_csv_path)
            self.assertIsInstance(data, pd.DataFrame)
        except Exception as e:
            self.fail(f"load_data raised an exception: {e}")

    def test_preprocess_data(self):
        processed_data = preprocess_data(self.data.copy())
        self.assertFalse(processed_data.isnull().values.any())
        self.assertTrue(processed_data['Date'].is_monotonic_increasing)

    def test_get_top_companies(self):
        top_companies = get_top_companies(self.data, n=1)
        self.assertEqual(len(top_companies), 1)
        self.assertIn('A', top_companies)

    def test_calculate_rolling_metrics(self):
        rolling_std = calculate_rolling_metrics(self.data, window=2, column='Close', metric='std')
        self.assertEqual(len(rolling_std), len(self.data))
        self.assertTrue(rolling_std.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
