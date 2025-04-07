**Assignment 1: Deploy a sample application on EC2 instance that should store data on RDS. Use AWS secrets manager for storing the connection strings**

 

### Step 1: Log in to AWS Management Console
1. Go to the [AWS Management Console](https://aws.amazon.com/console/).
2. Sign in with your AWS credentials.

### Step 2: Navigate to EC2
1. In the AWS Management Console, search for and select **EC2**.
2. Click on **Instances** in the left sidebar.

### Step 3: Launch a New Instance
1. Click on the **Launch Instance** button.
2. **Choose an Amazon Machine Image (AMI)**:
   - Select an AMI (e.g., Amazon Linux 2, Ubuntu Server).
3. **Choose an Instance Type**:
   - Select an instance type (e.g., t2.micro for free tier).
4. **Configure Instance**:
   - Click **Next: Configure Instance Details** and leave the default settings.
5. **Add Storage**:
   - Click **Next: Add Storage** and keep the default size.
6. **Configure Security Group**:
   - Click **Next: Configure Security Group**.
   - Create a new security group and allow:
     - SSH (port 22) from your IP address.
     - Custom TCP Rule (port 3306) for MySQL.
7. **Review and Launch**:
   - Click **Review and Launch**.
8. **Launch**:
   - Click **Launch** and select an existing key pair or create a new one for SSH access.
   ![alt text](../Week-4.images/WA(ec2).png)

### Step 4: Connect to Your EC2 Instance
1. Once the instance is running, select it and note the public IP address.
2. SSH into your EC2 instance:

### Step 5: Navigate to RDS
   - Select "RDS" and go to "Databases".
### Step 6: Select Your RDS Instance
   - Click on your RDS instance.
   ![alt text](../Week-4.images/WA(database).png)
### Step 7: Connect to Your RDS Instance
   - Use a MySQL client or command line to connect to the database.
### Step 8: Create the New Database
   - Run a command to create a new database.
   ![alt text](../Week-4.images/image.png)
### Step 9: Verify the Database Creation
   - Check the list of databases to confirm it was created.
### Step 10: Store Database Credentials in Secrets Manager
   - Navigate to "Secrets Manager" and create a new secret.
   - Add key-value pairs for username, password, host, port, and database name.
   ![alt text](../Week-4.images/WA(secrets).png)
### Step 11: Update Your Application
   - Ensure your application code retrieves the database name from Secrets Manager.
   # Application to Connect to RDS Using AWS Secrets Manager

```python
import boto3
import json
import pymysql

def main():
    client = boto3.client('secretsmanager', region_name='ap-south-1')  # Use your region here

    try:
        response = client.get_secret_value(SecretId="rds-connection-test")
        secret = json.loads(response['SecretString'])

        username = secret['username']
        password = secret['password']
        host = secret['host']
        port = int(secret['port'])
        dbname = secret.get('dbname')

        if not dbname:
            raise ValueError("The 'dbname' key is missing from the secret.")

        # Establishing the database connection
        connection = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=dbname,
            port=port
        )

        print("Connection established successfully!")

        cursor = connection.cursor()

        # Create a table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100)
            );
        """)
        print("Table 'users' checked/created successfully.")

        # Insert sample data
        cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com');")
        cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane.smith@example.com');")
        connection.commit()
        print("Sample data inserted successfully.")

        # Retrieve and display data
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        print("Data in 'users' table:")
        for row in rows:
            print(row)

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
### Step 12: Run Your Application
   - Execute your application to connect to the new database.
     ![alt text](../Week-4.images/WA(application_runned_successfully).png)
### Step 13: Create a CloudWatch Alarm

**1. Navigate to CloudWatch**
In the AWS Management Console, search for and select **CloudWatch**.

**2. Create an Alarm**
- Click on **Alarms** and then **Create Alarm**.
 ![alt text](../Week-4.images/day-4(alarm).png)
- Choose **Select metric** and navigate to **EC2 metrics**.
- Select **Per-Instance Metrics** and choose the **CPU utilization** metric for your instance.
- Click **Select metric**.

**3. Configure Alarm Settings**
- Set conditions for the alarm (e.g., whenever CPU utilization is greater than 80% for 5 minutes).
- Configure actions (e.g., send a notification to an SNS topic).
 ![alt text](../Week-4.images/day-4(subscription).png)

  ![alt text](../Week-4.images/Day-4(subscription-2).png)

 ![alt text](../Week-4.images/Day-4(topic).png)
**4. Name and Create Alarm**
- Provide a name and description for the alarm and click **Create alarm**.


  