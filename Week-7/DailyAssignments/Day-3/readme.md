**Assignment: Create config maps, secrets, and volumes and assign them to already created pods.**

First create a simple pod without any secret, config maps and volumes and expose the pod.

![alt text](../Day-3/service.png)

Now create config map and secrets and run kubectl create command:

![alt text](../Day-3/image.png)

Now delete the current pod and apply the changes in pod.yaml file and again create the pod using kubectl create command:

Now see the webpage:

![alt text](../Day-3/afterweb.png)