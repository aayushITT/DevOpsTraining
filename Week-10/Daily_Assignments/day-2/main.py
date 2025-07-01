import requests     # Used to send HTTP requests to the API
import argparse     # Used to handle command-line arguments
import json         # For saving data as JSON
import csv          # For writing data as CSV

# URL of the public API to fetch user data
URL = "https://randomuser.me/api/"

# Function to fetch data from the API
def fetch_data_from_api():
    try:
        response = requests.get(URL)         # Send GET request to API
        response.raise_for_status()          # Raise an exception for HTTP errors
        return response.json()["results"][0] # Extract the first user record from the results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")   # Print error if request fails
        return None                          # Return None if API call fails

# Function to save data into a JSON file
def save_data_as_json(file_path, data):
    with open(file_path, "w") as json_file:      # Open file in write mode
        json.dump(data, json_file, indent=4)     # Write JSON data to file with indentation

# Function to save data into a CSV file (with selected fields)
def save_data_as_csv(file_path, data):
    # Flatten nested data from API into a flat dictionary
    flat_data = {
        "first_name": data["name"]["first"],
        "last_name": data["name"]["last"],
        "email": data["email"],
        "city": data["location"]["city"],
        "country": data["location"]["country"],
        "username": data["login"]["username"]
    }

    with open(file_path, "w") as csv_file:               # Open file in write mode
        writer = csv.DictWriter(csv_file, fieldnames=flat_data.keys())  # Create CSV writer
        writer.writeheader()                             # Write header (column names)
        writer.writerow(flat_data)                       # Write one row of user data

# Main function to control the script logic
def main():
    parser = argparse.ArgumentParser(description="Fetch API data and save to file")
    parser.add_argument(
        "--filePath",
        required=True,
        help="Path to save data (.json or .csv)",
    )  # Add CLI argument for output file path
    args = parser.parse_args()               # Parse command-line arguments

    file_path = args.filePath                # Get file path from arguments
    data = fetch_data_from_api()             # Fetch user data from API

    if data is None:                         # If data fetching failed, stop the program
        return

    # Save data in the format based on file extension
    if file_path.endswith(".json"):
        save_data_as_json(file_path, data)
    elif file_path.endswith(".csv"):
        save_data_as_csv(file_path, data)
    else:
        raise ValueError("File type is not supported (use .json or .csv)")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
