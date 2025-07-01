import schedule  # For job scheduling (runs jobs at specific intervals)
import time      # To control sleep between job checks
import argparse  # For parsing command-line arguments
from disk_checker.cli import check_disk_usage  # Import the function to run periodically


# Job to be scheduled – runs the disk usage check
def job(threshold):
    print(f"\n[INFO] Running disk usage check with threshold {threshold}%...\n")
    check_disk_usage(threshold)


# Main function to parse CLI input and start scheduler
def main():
    parser = argparse.ArgumentParser(description="Run disk usage check every hour.")
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        required=True,
        help="Usage threshold percentage (e.g., 80)",  # Help text for user
    )
    args = parser.parse_args()  # Parse command-line arguments

    # Schedule the `job` function to run every hour with the provided threshold
    schedule.every().hour.do(job, threshold=args.threshold)

    print(
        f"[INFO] Scheduler started. Checking disk usage every hour with threshold {args.threshold}%..."
    )

    # Continuously check for pending scheduled jobs and run them
    while True:
        schedule.run_pending()  # Run any job whose time has come
        time.sleep(1)           # Sleep to avoid high CPU usage


# Entry point – runs main when the script is executed
if __name__ == "__main__":
    main()
