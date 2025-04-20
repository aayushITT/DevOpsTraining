**Assignment: Create Dockerfile to build and run .NET core application**

#### Run docker command to build image from dockerfile:
docker build -t my-dotnet-app .
![alt text](../Assignment-2/w6a2(docker%20build).png)

Create container from the image using command:
docker run -d -p 5000:5000 my-dotnet-app
![alt text](../Assignment-2/image.png)

See on web browser by searching  
http://localhost:5000/

![alt text](../Assignment-2/w6a2(webpage).png)



