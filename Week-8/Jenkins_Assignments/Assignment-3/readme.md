**Assignment: Create a freestyle job to deploy resources on AWS using terraform**

1. Install plugins : Terraform, AWS credentials

![alt text](../Assignment-3/1.png)

![alt text](../Assignment-3/2.png)

and access key and secret access key in jenkins manage > credetials > global section

![alt text](../Assignment-3/3.png)

2. Apply terraform installation from manage jenkins > tools

![alt text](../Assignment-3/4.png)

3. Add main.tf file to github repo

![alt text](../Assignment-3/5.png)

4. Create a freestyle job with configure:

**SCM as git with github url**

![alt text](../Assignment-3/6.png)

**Use aws secret credentials**

![alt text](../Assignment-3/7.png)

**Select terraform checkbox in environment section**

![alt text](../Assignment-3/8.png)

**Add build steps in build section**

![alt text](../Assignment-3/9.png)

5. See the output on aws console

![alt text](../Assignment-3/instance.png)