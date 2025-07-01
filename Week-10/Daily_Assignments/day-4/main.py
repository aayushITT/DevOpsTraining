import requests  # For making HTTP requests
import argparse  # For handling CLI arguments
import json  # For working with JSON data
import csv  # For working with CSV files
import logging  # For logging messages
from logging.handlers import RotatingFileHandler  # To manage rotating log files

# API URL to fetch user data
URL = "https://jsonplaceholder.typicode.com/users/1"

# Set up logger for the module
logger = logging.getLogger("__main__")  # Create a logger object
logger.setLevel(logging.INFO)  # Set log level to INFO

# Console handler for output on screen
consoleHandler = logging.StreamHandler()

# File handler with rotation: keeps backup logs and limits file size
fileHandler = RotatingFileHandler("test.log", backupCount=100, maxBytes=1024)

# Define formatter for logs
consoleFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Attach formatter to handlers
consoleHandler.setFormatter(consoleFormatter)
fileHandler.setFormatter(consoleFormatter)

# Add handlers to logger
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


# Function to fetch data from public API
def fetch_data_from_api():
    try:
        response = requests.get(URL)  # Make GET request to API
        response.raise_for_status()  # Raise error for bad status codes
        logger.info("Response Taken from URL.")  # Log success
        return response.json()  # Return response data as JSON
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from URL: {str(e)}")
        return None


# Save the fetched data to a JSON file
def save_data_as_json(file_path, data):
    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully written to JSON file: {file_path}")
    except Exception as e:
        logger.error(f"Error saving JSON file: {str(e)}")


# Save the fetched data to a CSV file
def save_data_as_csv(file_path, data):
    try:
        with open(file_path, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())  # Uses data keys as column headers
            writer.writeheader()
            writer.writerow(data)  # Write a single row of data
        logger.info(f"Data successfully written to CSV file: {file_path}")
    except Exception as e:
        logger.error(f"Error saving CSV file: {str(e)}")


# Main function executed from CLI
def main():
    parser = argparse.ArgumentParser()  # Create argument parser
    parser.add_argument(
        "--filePath",
        required=True,
        help="Add file path for storing data. File type must be either csv or json",
    )
    args = parser.parse_args()
    file_path = args.filePath  # Get file path from CLI
    logger.info(f"File path received: {file_path}")

    data = fetch_data_from_api()  # Call API and fetch data

    if data is None:
        logger.warning("No data fetched from API. Exiting.")  # Exit if API failed
        return

    # Depending on file extension, save data accordingly
    try:
        if file_path.endswith(".json"):
            save_data_as_json(file_path, data)
        elif file_path.endswith(".csv"):
            save_data_as_csv(file_path, data)
        else:
            raise ValueError("File type is not supported (use .json or .csv)")
    except Exception as e:
        logger.error(f"Error in saving data: {str(e)}")


# Run main() if this script is executed
if __name__ == "__main__":
    main()
