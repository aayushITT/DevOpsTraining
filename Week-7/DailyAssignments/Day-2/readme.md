**Assignment: Create a pod with a basic HTML page and service to expose that pod.**

Create a configMap with html-configMap.yaml file using command:

```kubectl create -f html-configMap.yaml```

Create a pod with html-pod.yaml file using command:

```kubectl create -f html-pod.yaml```

Create service with html-service.yaml file using command:

```kubectl create -f html-service.yaml```

![alt text](../Day-2/apply.png)

Now run command:

```minikube service <service_name>```

![alt text](../Day-2/get.png)

Redirect to url http://127.0.0.1:33009

![alt text](../Day-2/webpage.png)