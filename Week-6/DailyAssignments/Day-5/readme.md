# **Assignment: Create two containers and both the containers should share the common volume**

## Steps Using Docker CLI

### 1. Create a Docker Volume

```bash
docker volume create shared-vol
```

---
![alt text](../Day-5/Day-5(shared%20volume).png)

### 2. Run the First Container and Attach the Volume

```bash
docker run -it --name container1 -v shared-vol:/data ubuntu
```

Inside `container1`, run:

```bash
echo "Hello from Container 1" > /data/hello.txt
exit
```
![alt text](../Day-5/Day-5(running%20first%20container).png)

---

### 3. Run the Second Container with the Same Volume

```bash
docker run -it --name container2 -v shared-vol:/data ubuntu
```

Inside `container2`, run:

```bash
cat /data/hello.txt
```
![alt text](../Day-5/Day-5(run%202nd%20container).png)

You should see:

```
Hello from Container 1
```

This confirms that both containers are sharing the same volume.

---

## &#x20;

