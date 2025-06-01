import requests
import argparse
import json
import csv
import logging
from logging.handlers import RotatingFileHandler

URL = "https://jsonplaceholder.typicode.com/users/1"

# URL = "abcd"

logger = logging.getLogger("__main__")
logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
fileHandler = RotatingFileHandler("test.log", backupCount=100, maxBytes=1024)
consoleFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
consoleHandler.setFormatter(consoleFormatter)
fileHandler.setFormatter(consoleFormatter)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


def fetch_data_from_api():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        logger.info(f"Response Taken from URL.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from URL: {str(e)}")
        return None


def save_data_as_json(file_path, data):
    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully written to JSON file: {file_path}")
    except Exception as e:
        logger.error(f"Error saving JSON file: {str(e)}")


def save_data_as_csv(file_path, data):
    try:
        with open(file_path, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        logger.info(f"Data successfully written to CSV file: {file_path}")
    except Exception as e:
        logger.error(f"Error saving CSV file: {str(e)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filePath",
        required=True,
        help="Add file path for storing data. File type must be either csv or json",
    )
    args = parser.parse_args()

    file_path = args.filePath
    logger.info(f"File path received: {file_path}")

    data = fetch_data_from_api()

    if data is None:
        logger.warning("No data fetched from API. Exiting.")
        return

    try:
        if file_path.endswith(".json"):
            save_data_as_json(file_path, data)
        elif file_path.endswith(".csv"):
            save_data_as_csv(file_path, data)
        else:
            raise ValueError("File type is not supported (use .json or .csv)")
    except Exception as e:
        logger.error(f"Error in saving data: {str(e)}")


if __name__ == "__main__":
    main()