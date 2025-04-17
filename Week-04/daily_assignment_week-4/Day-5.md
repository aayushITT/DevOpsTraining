**Assignment: Explore different Backup and Disaster recovery approaches and understand how to take and restore the backups of EFS, EBS, and RDS.**

**Take and Restore backup of EBS volume:**

1. Snapshots:

How to take backup: 

Step 1. Select EC2 service of AWS and click on volumes.

Step 2. Select the volume and click on actions and select create snapshot.

Step 3. Enter snapshot description and click on create snapshot.

Backup of particular EBS is taken in terms of snapshot.

Hot to restore the backup:

Step 1. Once after the snapshot status is COMPLETED, select the snapshot and click on actions and select create volume from snapshot.

Step 2. Add EBS volume details and increase the size from original EBS volume if required. 

Step 3. Click on create volume and now new EBS volume is restored from previous one.

Step 4. Attach this new EBS volume to new EC2 server and continue tasks after mouting it.

2. AWS backup

How to take backup:

Step 1. Select AWS backup service and click on create backup plan.

Step 2. Add backup plan name and add backup rule, backup frequency and backup window. Select default backup vault or create new backup vault and add to it. Finally select create plan.

Step 3. Under the backup plan click on assign resources.

Step 4. Add assign resource name, select default IAM role and then choose resource type as EBS and click on add resource to add EBS volume, Click on assign resource.

AWS Backup will now automatically create EBS backups based on the defined schedule.

How to restore the backup:

Step 1. In AWS backup console select the backup vault choosen to store the backup.

Step 2. Click on recovery points and find the latest backup.

Step 3. Select the backup recovery point id and click on restore and aaply the configuration required(volume type and availability zone).

Step 4. Click on restore backup.

AWS will create a new EBS volume from the backup

Attach Restored Volume to an EC2 Instance.


**Take and Restore backup of EFS:**

1. AWS backup

How to take backup:

Step 1. Select AWS backup service from the AWS console and click on create backup plan.

Step 2. Add backup plan name and add backup rule, backup frequency and backup window. Select default backup vault or create new backup vault and add to it. 

Step 3. Under "Resources to Backup", select EFS file system and finally select create plan.

AWS Backup will now take daily incremental backups of your EFS.

How to restore backup:

Step 1. Go to backup vault choosen for EFS backup and select the latest backup and click restore.

Step 2. Restore the backup to new or existing EFS. If existing EFS then no need to mount the EFS again to instances, if backup to new EFS then need to explicitly mount the EFS again in instances.

Step 3. Click on restore backup.


**Take and Restore backup of RDS:**

1. Enable automated backups

RDS automatically takes backups daily and keeps transaction logs for point-in-time recovery.

How to take backup:

Step 1. Select RDS service of AWS and choose your DB instance.

Step 2. Click on modify and under backup retention period choose 1-35 days.

Step 3. Under backup window specify a time when backups should be taken.

Step 4. Click on continue and apply immediately.

How to restore backups:

Step 1. Go to AWS Console and select RDS, click Actions and restore to Point in Time.

Step 2. Choose the date and time to restore, finally click Restore DB Instance.

2. Take manual RDS snapshots

How to take backup:

Step 1. Select your DB instance and click on actions.

Step 2. Select snapshot and enter name of snapshot and click on create snapshots.

How to recover backups:

Step 1. Go to AWS Console and select RDS.

Step 2. Click Snapshots and select your Manual Snapshot.

Step 3. Click Actions and restore Snapshot.

Step 4. Enter a New DB Instance Name and click Restore DB Instance.

Manual snapshots do not expire until you manually delete them.

3. AWS backup

How to take backup:

Step 1. Select AWS backup service from the AWS console and click on create backup plan.

Step 2. Add backup plan name and add backup rule, backup frequency and backup window. Select default backup vault or create new backup vault and add to it. 

Step 3. Under "Resources to Backup", select RDS and finally select create plan.