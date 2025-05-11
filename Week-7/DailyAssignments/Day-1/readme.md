**Assignment: Create a basic minikube cluster on local system. Create a namespace and deploy an ubuntu POD in it.**

Run the following commands:

Initialize minikube
minikube start

![alt text](../Day-1/d1(minikube-start).png)

Create namespace
kubectl create namespace my-namespace

![alt text](../Day-1/d1(namespace).png)

Create yaml file for pod creation

![alt text](../Day-1/d1(pod.yml).png)

Run the following command to create pod
kubectl apply -f <pod_file_name>

![alt text](../Day-1/d1(apply%20pod).png)

 verify pod

![alt text](../Day-1/d1(get%20pods).png)


