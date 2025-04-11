Assignment: Deploy a static web application on EC2 instance using modularized Terraform code. The backend should be configured in S3

Before backend.tf file created

Run the following commands:

terraform init
terraform plan
terraform apply
So s3 bucket is created:
![alt text](../Weekly_Assignment/w5(bucket).png)

EC2 instance is created

![alt text](../Weekly_Assignment/w5(ec2).png)

Now create backend.tf file and run the command:

terraform init

state file is added to s3 bucket

![alt text](../Weekly_Assignment/w5(webpage).png)