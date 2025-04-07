**Assignment: Explore Cloudfront and showcase ALB as origin to it**

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.


Step 1. Create 2 EC2 instance from different region (us-east-1).

Step 2. Create a target group with those 2 instances.

Step 3. Create application load balancer with default security group and above target group and click on create load balancer.

Step 4. Update the security group of EC2 instances so that inbound traffic can come from load balancer only. So add ALB security group to EC2 inbound traffic for HTTP protocol.

Step 5. Create Cloud front distribution, choose origin(EC2 public domain), name and set WAf to disable and create cloud distribution.

Step 6. Update ALB security group with inbound traffic of http to managed prefix list of cloudfront origin-facing.

Now copy distribution domain name from cloudfront and run on browser.

For the first time if you inspect and see it will be shown **Miss from CloudFront**

![alt text](../Week-4.images/day-3(cloud-miss).png)

Next Time again you refresh and it will show **Hit from cloudfront**

![alt text](../Week-4.images/Screenshot%202025-04-04%20145320.png)