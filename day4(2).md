# Steps to Create an S3 Bucket and Set Up Cross-Account Replication

## Account A: Source Bucket

### Step 1: Create S3 Bucket
- Log in to **Account A**.
- Navigate to **S3** and create a bucket (e.g., `source-bucket`).
- Enable **versioning** in the bucket properties.

### Step 2: Set Bucket Policy
- Go to **Permissions > Bucket Policy** and add a policy to allow Account B to replicate objects:
- Replace `<ACCOUNT_B_ID>` with the actual Account B ID.

---

## Account B: Destination Bucket

### Step 3: Create S3 Bucket
- Log in to **Account B**.
- Navigate to **S3** and create a bucket (e.g., `destination-bucket`).
- Enable **versioning** in the bucket properties.

### Step 4: Set Up KMS Key (Optional)
- If using KMS encryption:
- Create a KMS key in **Account B**.
- Grant permissions to **Account A** to use the KMS key:
  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "AWS": [
                      "<ACCOUNT_A_IAM_ROLE_ARN>"
                  ]
              },
              "Action": [
                  "kms:Encrypt",
                  "kms:ReEncrypt*",
                  "kms:GenerateDataKey*",
                  "kms:DescribeKey"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

### Step 5: Set Bucket Policy
- Go to **Permissions > Bucket Policy** and add a policy to allow Account A to write objects:
- Replace `<ACCOUNT_A_IAM_ROLE_ARN>` with the actual IAM Role ARN from Account A.

---

## Set Up Cross-Account Replication

### Step 6: Enable Cross-Account Replication
- Go back to the **source bucket** in Account A.
- Navigate to **Management > Replication > Add rule**.
- Configure the following:
- Select whether to replicate all objects or specific prefixes.
- Provide the ARN of the destination bucket in Account B.
- Select or create an IAM role for replication.

### Step 7: Review and Save
- Review the replication configuration and save the settings.

---
 
