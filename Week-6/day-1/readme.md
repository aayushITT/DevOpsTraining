
**Assignment: Docker commands to run any command inside the container and close the container.**

Download image of ubuntu from public registry like DockerHUB using command:

# docker pull ubuntu

Command to run command inside ubuntu container:

# docker run --<name_of_container> ubuntu <command>

# docker run --name MyContainer ubuntu echo "Hello from MyContainer"

![alt text](../day-1/day-1(commandinsideconatainer).png)