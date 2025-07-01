import unittest  # Python built-in module for unit testing
import os  # To interact with the file system
import json  # To handle JSON file read/write
import csv  # To handle CSV file read/write

# Importing the actual functions to test from the main script
from main import fetch_data_from_api, save_data_as_json, save_data_as_csv


# Define a test class that inherits from unittest.TestCase
class TestWithoutMock(unittest.TestCase):

    # Setup runs before each test
    def setUp(self):
        self.json_file = "test_output.json"  # Path for test JSON output
        self.csv_file = "test_output.csv"  # Path for test CSV output
        self.sample_data = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe"
        }  # Sample dictionary data used for testing

    # Teardown runs after each test to clean up
    def tearDown(self):
        # Remove the JSON file if it was created during the test
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        # Remove the CSV file if it was created during the test
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    # Test fetching data from a real API (not mocked)
    def test_fetch_data_from_api_real(self):
        data = fetch_data_from_api()  # Call actual function
        self.assertIsInstance(data, dict)  # Check if returned data is a dictionary
        self.assertIn("id", data)  # Check if 'id' key exists in the response

    # Test saving JSON data to file and verifying its contents
    def test_save_data_as_json_real(self):
        save_data_as_json(self.json_file, self.sample_data)  # Save sample data to JSON
        self.assertTrue(os.path.exists(self.json_file))  # Ensure file was created
        with open(self.json_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, self.sample_data)  # Verify content matches original

    # Test saving CSV data to file and verifying its contents
    def test_save_data_as_csv_real(self):
        save_data_as_csv(self.csv_file, self.sample_data)  # Save sample data to CSV
        self.assertTrue(os.path.exists(self.csv_file))  # Ensure file was created
        with open(self.csv_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)  # Read all rows into a list
        self.assertEqual(len(rows), 1)  # Ensure there's only one row
        self.assertEqual(rows[0]["first_name"], "John")  # Verify data correctness


# Execute tests when this script is run directly
if __name__ == "__main__":
    unittest.main()
