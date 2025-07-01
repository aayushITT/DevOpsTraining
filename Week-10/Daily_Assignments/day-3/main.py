import paramiko  # Library for SSH connections
import logging  # Library for logging messages

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    filemode="a",  # Append logs to the file
    filename="disk_usage.log",  # Log file name
)

DISK_THRESHOLD = 40  # Disk usage percentage threshold for alerts

# SSH connection details for the remote server
hostname = "13.201.99.182"  # Public IP or DNS of remote server
port = 22  # SSH port
username = "ubuntu"  # SSH username
private_key_path = r"C:\Users\aayush.s\Downloads\my-new-ec2-29.pem"  # Path to private key for authentication

# Create an SSH client object
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept unknown host keys

try:
    # Connect to the remote server using SSH
    ssh_client.connect(
        hostname=hostname,
        port=port,
        username=username,
        key_filename=private_key_path,
    )

    # Run the disk usage command and process the result
    stdin, stdout, stderr = ssh_client.exec_command(
        "df -h | awk 'NR>1 {gsub(/ /, \"\", $5); print $1, $5}'"
    )
    output = stdout.read().decode()  # Read command output
    error = stderr.read().decode()  # Read any errors

    if error:
        print("Error: ", error)  # Print error if any

    if output:
        usage_info = []
        for line in output.splitlines():  # Iterate over each disk line
            disk, usage_str = line.split()
            usage_percent = int(usage_str.replace("%", ""))  # Convert usage to int
            usage_info.append((disk, usage_percent))  # Append disk info to list

        # Check disk usage against threshold and log warnings
        for disk, usage_percent in usage_info:
            if usage_percent > DISK_THRESHOLD:
                logging.warning(
                    f"{disk} is using {usage_percent}% which is exceeding the threshold."
                )

finally:
    ssh_client.close()  # Always close SSH connection after execution
