import json
import yaml
import logging
import argparse
import os

# Function to initialize and configure logging
def add_logs(file_path):
    os.makedirs(
        os.path.dirname(file_path), exist_ok=True
    )  # Create log directory if it doesn't exist
    logging.basicConfig(
        level=logging.INFO,                 # Set logging level to INFO
        filename=file_path,                 # Log file path
        filemode="a",                       # Append to the log file if it exists
        format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
    )
    logging.info("Logger Initialized")     # Log an initialization message

# Function to read a configuration file (YAML or JSON)
def read_config_file(file_path):
    with open(file_path, "r") as file:     # Open the config file in read mode
        if file_path.endswith(".yaml") or file_path.endswith(".yml"):
            return yaml.safe_load(file)    # Parse YAML file and return as dictionary
        elif file_path.endswith(".json"):
            return json.load(file)         # Parse JSON file and return as dictionary
        else:
            # Raise error for unsupported file types
            raise ValueError("Config file type is not supported.")

# Main function to parse arguments and execute logic
def main():
    default_log_path = "./logs/app.log"  # Default path to log file if not specified

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Read config and write logs.")
    parser.add_argument(
        "--ConfigfilePath", required=True, help="Path to config file (.json or .yaml)"
    )  # Required argument for config file path
    parser.add_argument(
        "--LogFilePath", default=default_log_path, help="Path to log file"
    )  # Optional log file path with a default

    args = parser.parse_args()  # Parse command-line arguments

    try:
        add_logs(args.LogFilePath)  # Initialize logging using specified log file path
        config = read_config_file(args.ConfigfilePath)  # Load config file contents
        logging.info(f"Successfully read config from {args.ConfigfilePath}")
        logging.info(f"Config file content: {config}")  # Log config content
    except Exception as e:
        # Log and print any error that occurs during execution
        logging.error(f"Error: {str(e)}")
        print(f"Error: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    main()
