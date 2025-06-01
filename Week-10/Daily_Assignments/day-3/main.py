import paramiko
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a",
    filename="disk_usage.log",
)

DISK_THRESHOLD = 40

hostname = "13.201.99.182"
port = 22
username = "ubuntu"
private_key_path = r"C:\Users\aayush.s\Downloads\my-new-ec2-29.pem"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(
        hostname=hostname, port=port, username=username, key_filename=private_key_path
    )
    stdin, stdout, stderr = ssh_client.exec_command(
        "df -h | awk 'NR>1 {gsub(/ /, \"\", $5); print $1, $5}'"
    )
    output = stdout.read().decode()
    error = stderr.read().decode()

    if error:
        print("Error: ", error)

    if output:
        usage_info = []
        for line in output.splitlines():
            disk, usage_str = line.split()
            usage_percent = int(usage_str.replace("%", ""))
            usage_info.append((disk, usage_percent))

        for disk, usage_percent in usage_info:
            if usage_percent > DISK_THRESHOLD:
                logging.warning(
                    f"{disk} is using {usage_percent}% which is exceeding the threshold."
                )


finally:
    ssh_client.close()