Assignment: Import an existing resource from AWS in Terraform state file

Already existing EC2 instance on AWS cloud:

![alt text](../Day-4/W5D4(ec2).png)

Run command to initialize the plugins with empty resource block

terraform init

Copy instance id from AWS cloud and run terraform import command:

terraform import <resource_type>.<resource_name>
![alt text](../Day-4/W5D4(import).png)

We can check the current state using this command, it consist of my EC2 instance state:

terraform show

Now add arguments of your instance according to provided in AWS cloud

Now if we run plan or apply command it will give "No changes"

![alt text](../Day-4/W5D4(terraform%20plan).png)
![alt text](../Day-4/W5D4(terraform%20apply).png)
![alt text](../Day-4/W5D4(verified%20import).png)