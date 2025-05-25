**Assignment: Create an Azure Key Vault and store the following: A certificate, A secret (e.g., a database connection string)**

1. Create Azure key vault:

Step 1: Go to azure portal and cselect key vault service.

![alt text](1.png)

Step 2: Click on create key vault and add basic information.

![alt text](2.png)

Step 3: Click on review and create.

![alt text](3.png)

2. Add self signed certificate.

Step 1: Select objects > certificate in left side bar menu of key vault.

![alt text](4.png)

Step 2: Click on Access control(IAM) and click on role assignment.

Step 3: Add role as key vault administrator and select you as member.

![alt text](5.png)

![alt text](6.png)

Step 4: Click on generate and import and fill in the detials and choose self signed certificate.

![alt text](7.png)

Step 5: Certificat is created.

![alt text](8.png)



3. A secret

Step 1: Click on object > secret in left side bar menu.

![alt text](9.png)

Step 2: Click on generate import secret.

![alt text](10.png)

Step 3: Click on create secret.

![alt text](11.png)