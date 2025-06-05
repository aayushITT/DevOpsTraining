import unittest
import os
import json
import csv

from main import fetch_data_from_api, save_data_as_json, save_data_as_csv


class TestWithoutMock(unittest.TestCase):

    def setUp(self):
        self.json_file = "test_output.json"
        self.csv_file = "test_output.csv"
        self.sample_data = {"id": 1, "first_name": "John", "last_name": "Doe"}

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_fetch_data_from_api_real(self):
        data = fetch_data_from_api()
        self.assertIsInstance(data, dict)
        self.assertIn("id", data)

    def test_save_data_as_json_real(self):
        save_data_as_json(self.json_file, self.sample_data)
        self.assertTrue(os.path.exists(self.json_file))
        with open(self.json_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content, self.sample_data)

    def test_save_data_as_csv_real(self):
        save_data_as_csv(self.csv_file, self.sample_data)
        self.assertTrue(os.path.exists(self.csv_file))
        with open(self.csv_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["first_name"], "John")


if __name__ == "__main__":
    unittest.main()