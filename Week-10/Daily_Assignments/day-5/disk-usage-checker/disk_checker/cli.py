import argparse
import subprocess


def check_disk_usage(threshold):
    result = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True)
    output = result.stdout
    print(f"\nDisks exceeding {threshold}% usage:\n")

    header = True
    for line in output.splitlines():
        if header:
            header = False
            continue

        row = line.split()
        percent_used = row[4].replace("%", "")
        mount_point = row[5]

        try:
            percent_used = int(percent_used)
            if percent_used > threshold:
                print(f"{mount_point} is at {percent_used}% usage")
        except ValueError:
            continue


def main():
    parser = argparse.ArgumentParser(
        description="Check disk usage of machine with ubuntu OS.",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        required=True,
        help="Usage threshold percentage (e.g., 80)",
    )
    args = parser.parse_args()
    check_disk_usage(args.threshold)


if __name__ == "__main__":
    main()