import schedule
import time
import argparse
from disk_checker.cli import check_disk_usage


def job(threshold):
    print(f"\n[INFO] Running disk usage check with threshold {threshold}%...\n")
    check_disk_usage(threshold)


def main():
    parser = argparse.ArgumentParser(description="Run disk usage check every hour.")
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        required=True,
        help="Usage threshold percentage (e.g., 80)",
    )
    args = parser.parse_args()

    # Schedule the job every hour
    schedule.every().hour.do(job, threshold=args.threshold)

    print(
        f"[INFO] Scheduler started. Checking disk usage every hour with threshold {args.threshold}%..."
    )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()