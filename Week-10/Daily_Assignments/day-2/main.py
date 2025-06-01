import requests
import argparse
import json
import csv

URL = "https://randomuser.me/api/"  # Updated to a working public API


def fetch_data_from_api():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()["results"][0]  # Extract first user object
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def save_data_as_json(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)


def save_data_as_csv(file_path, data):
    # Flatten nested JSON to write into CSV
    flat_data = {
        "first_name": data["name"]["first"],
        "last_name": data["name"]["last"],
        "email": data["email"],
        "city": data["location"]["city"],
        "country": data["location"]["country"],
        "username": data["login"]["username"]
    }

    with open(file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=flat_data.keys())
        writer.writeheader()
        writer.writerow(flat_data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filePath",
        required=True,
        help="Add file path for storing data. File type must be either csv or json",
    )
    args = parser.parse_args()

    file_path = args.filePath
    data = fetch_data_from_api()

    if data is None:
        return

    if file_path.endswith(".json"):
        save_data_as_json(file_path, data)
    elif file_path.endswith(".csv"):
        save_data_as_csv(file_path, data)
    else:
        raise ValueError("File type is not supported (use .json or .csv)")


if __name__ == "__main__":
    main()
