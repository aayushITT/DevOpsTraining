import json
import yaml
import logging
import argparse
import os


def add_logs(file_path):
    os.makedirs(
        os.path.dirname(file_path), exist_ok=True
    )  # make log directory if not present
    logging.basicConfig(
        level=logging.INFO,  # logging level
        filename=file_path,  # path of file where logs are appended
        filemode="a",  # logs are appended
        format="%(asctime)s - %(levelname)s - %(message)s",  # format in which logs are appended
    )

    logging.info("Logger Initialized")  # just printing a logger initialized line


def read_config_file(
    file_path,
):  # function used for reading config file. Path of file is passed as argument
    with open(
        file_path, "r"
    ) as file:  # open the file from file path in read mode as file
        if file_path.endswith(".yaml") or file_path.endswith(
            ".yml"
        ):  # checks is the file path ends with yaml or json
            return yaml.safe_load(file)  # converts the yaml data to python dictionary
        elif file_path.endswith(".json"):
            return json.load(file)  # converts the json data to python dictionary
        else:
            raise ValueError(
                "Config file type is not supported."
            )  # if file type is not json, yaml or yml


def main():
    default_log_path = "./logs/app.log"  # default log path
    parser = argparse.ArgumentParser()  # creating argparse object as parser
    parser.add_argument(
        "--ConfigfilePath", required=True, help="Path to config file"
    )  # adding config file path as argument
    parser.add_argument(
        "--LogFilePath", default=default_log_path, help="Path of log file"
    )  # adding log file path as argument

    args = parser.parse_args()

    try:
        add_logs(args.LogFilePath)  # passing log file path to add_logs function
        config = read_config_file(
            args.ConfigfilePath
        )  # reading config file and storing in config variable
        logging.info(f"Successfully read config from {args.ConfigfilePath}")
        logging.info(
            f"Config file content: {config}"
        )  # passing content of config file from config variable to logger
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()