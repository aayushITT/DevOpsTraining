**Assignment: Create a Lambda function in Python that automatically copies images from the source  S3 bucket to the destination S3 bucket as soon as they gets uploaded in the source bucket.**

**1. Create source and destination S3 buckets:**

Step 1. Search S3 from AWS console search bar and click on create bucket.

Step 2. Enter name of bucket and leave all the configurations to default and click on create bucket.

Step 3. Repeat same step for creating destination bucket 

![alt text](../Week-4.images/day-2.1(buckets).png)

**2. Create an IAM Role for Lambda:**

Step 1. Search IAM from AWS console search bar and click on IAM.

Step 2. Click on create role and choose AWS service as lambda and click on create role.

Step 3. Add inline policy to the role :

![alt text](../Week-4.images/day-2.1(roles).png)

![alt text](../Week-4.images/day-2.2(role-created).png)

Created role.
 

**3. Create lambda function:**

Step 1. Select lambda service and click on create function.

Step 2. Add name to the function and choose python language and in permission attach role created.

Step 3. Add following code in the code and section and click on deploy:

<>

import json
import urllib.parse
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Event received:", json.dumps(event, indent=2))

    # Extract bucket name and object key from event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    # Define destination bucket
    destination_bucket = "destination-bucket-demo"

    try:
        # Copy the object
        copy_source = {'Bucket': source_bucket, 'Key': object_key}
        s3.copy_object(Bucket=destination_bucket, Key=object_key, CopySource=copy_source)

        print(f"Successfully copied {object_key} from {source_bucket} to {destination_bucket}")
        return {
            'statusCode': 200,
            'body': json.dumps(f"File {object_key} copied successfully!")
        }
    except Exception as e:
        print(f"Error copying object: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps("Error copying file")
        }

</>

![alt text](../Week-4.images/day-2.3(lambda%20function).png)

**4. Configure S3 trigger:**

Step 1. Click on trigger and add trigger.

Step 2. Select service as S3 and add source bucket name and in suffix section add .jpg for image file only.

Step 3. Create multiple trigger for .png and .jpeg.

![alt text](../Week-4.images/day-2(added%20trigger).png)

**5. Test the setup:**

Upload any .jpg file to source bucket and see the file gets copied in destination bucket also.

Only file ending with extension .jpg, .png and .jpeg will be copied.
 