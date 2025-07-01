import argparse  # For parsing command-line arguments
import subprocess  # To run shell commands like `df -h`


# Function to check disk usage and print any that exceed the given threshold
def check_disk_usage(threshold):
    # Run the 'df -h' command and capture its output
    result = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True)
    output = result.stdout  # Get the command output as a string

    print(f"\nDisks exceeding {threshold}% usage:\n")

    header = True  # Used to skip the header row in the 'df' output
    for line in output.splitlines():
        if header:
            header = False  # Skip the first header line
            continue

        row = line.split()  # Split the line into parts (filesystem, size, used, etc.)
        percent_used = row[4].replace("%", "")  # Extract the usage percentage
        mount_point = row[5]  # Get the mount point (e.g., /, /home, etc.)

        try:
            percent_used = int(percent_used)  # Convert percentage to integer
            # If usage exceeds the threshold, print a warning
            if percent_used > threshold:
                print(f"{mount_point} is at {percent_used}% usage")
        except ValueError:
            continue  # If conversion fails, skip this line


# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(
        description="Check disk usage of machine with ubuntu OS.",
    )
    parser.add_argument(
        "-t",  # Short flag
        "--threshold",  # Long flag
        type=int,  # Accepts an integer value
        required=True,  # Must be provided
        help="Usage threshold percentage (e.g., 80)",  # Help text for the argument
    )
    args = parser.parse_args()  # Parse arguments from CLI
    check_disk_usage(args.threshold)  # Call the disk check function with threshold


# Standard way to run the script directly
if __name__ == "__main__":
    main()
