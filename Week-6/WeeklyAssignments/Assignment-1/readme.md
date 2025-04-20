# **Assignment: Create custom Dockerfile for running a sample html website**

 

## Steps:

### 1. Create Project Directory

```bash
mkdir my-html-website
cd my-html-website
```
#### Create index.html file for static web page
![alt text](../Assignment-1/w6a1(index.html).png)

#### Create Dockerfile to build image for static web page:

![alt text](../Assignment-1/w6a1(dockerfile).png)


#### Build image using command:
docker build -t my-html-website .
![alt text](../Assignment-1/w6a1(build%20docker%20image).png)



#### Build the container from the image using command:
docker run -d -p 8080:80 my-html-website

![alt text](../Assignment-1/w6a1(docker%20run).png)


Check browser on http://localhost:8080

![alt text](../Assignment-1/w6a1(sample%20website).png)


