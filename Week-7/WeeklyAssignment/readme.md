**Assignment: Use the ECR image created for the .Net application and deploy it on minikube. The Application in the pod should be accessible on the browser. Assign suitable resource limits and requests on namsepace and deployment levels respectively.**

Docker image is created from dockerfile using command:

``` docker build -t dotnet-image .```

Image is pushed to ECR using commands:

```aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 536697246803.dkr.ecr.ap-south-1.amazonaws.com```

```docker tag new_dotnet_image:latest 536697246803.dkr.ecr.ap-south-1.amazonaws.com/new_dotnet_image:latest```

```docker push 536697246803.dkr.ecr.ap-south-1.amazonaws.com/new_dotnet_image:latest```

Now starting minikube on local machine:
```minikube start```

Login to ECR using command:
```aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 536697246803.dkr.ecr.ap-south-1.amazonaws.com```

![alt text](../WeeklyAssignment/1.png)

Create namespace and resourcequota from namespace.yaml file using command:

```kubectl apply -f namespace.yaml```

![alt text](../WeeklyAssignment/2.png)

Create secret for docker configuration using command:

```kubectl create secret generic awsecr-cred-secret --type=kubernetes.io/dockerconfigjson --from-file=.dockerconfigjson=$HOME/.docker/config.json --namespace=dotnet-app```

![alt text](../WeeklyAssignment/3.png)

Create deployment from deployment.yaml file using command:

```kubectl apply -f deployment.yaml```

![alt text](../WeeklyAssignment/4.png)

Expose the deployment or pods to browser from service.yaml file using command:

```kubectl apply -f service.yaml```

![alt text](../WeeklyAssignment/5.png)

We can see the pods in running status:

![alt text](../WeeklyAssignment/6.png)

Now run the command:

```minikube service helloworld-service -n dotnet-app```

![alt text](../WeeklyAssignment/7.png)

Now run http://127.0.0.1:35441 on browser and check:

![alt text](../WeeklyAssignment/8.png)