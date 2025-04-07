 **Assignment : Create alarm in cloudwatch on the basis of average CPU utilisation for a VM**

**1. Create an EC2 instance:**

Step 1. Select EC2 service of AWS and click on launch instance.

Step 2. Add name to EC2 instance "Demo" and attach key pair to it and launch an EC2 instance with basic confirguration.

![alt text](../Week-4.images/day-4(ec2).png)

**2. Create an alarm:**

Step 1. Select Cloudwatch service of AWS and select alarms from left side bar.

Step 2. Click in create alarm and click on select metric.

Step 3. Choose region -> EC2 service -> per-instance metrics -> select row having Demo (instance name) and CPU utilization (metric name) and click on Click on select metric.

Step 4. Add Statistics and Period according to requirement and in condition choose CPU utilization greator then 80% and move next.

Step 5. Select Alarm state trigger - In alarm and click on create SNS topic and add name of topic and mail id of user to whome the alarm is to be sent.

Step 6. The user will receive an email to confirm so user must confirm the email.

Step 7. Add name and description of alarm and click on create alarm.
![alt text](../Week-4.images/day-4(alarm).png)


**3. Connect to EC2 instance and check CPU utilization:**

Step 1. SSH to EC2 instance and run this command to check CPU utilization:

# top

Step 2. Check CPU utilization 

**4. Manually increase the CPU utilization and check the alarm status:**

Currently alarm status is ok:

Run this command to increase the CPU utilization

# yes > /dev/null &

this will increase the CPU utilization


After a particular period set for alarm the status will be changed to "In Alarm":



A email is sent to the user for excess CPU utilization.

![alt text](../Week-4.images/day-4(subscription).png)

![alt text](../Week-4.images/Day-4(subscription-2).png)


![alt text](../Week-4.images/Day-4(topic).png)

To Reduce the CPU utlization enter these commands:

# ps aux | grep yes

copy the id 

# kill id