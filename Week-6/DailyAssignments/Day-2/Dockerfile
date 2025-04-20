# Use the base image
FROM ubuntu:latest

# Update package lists
RUN apt-get update

# Upgrade existing packages and install curl
RUN apt-get upgrade -y && apt-get install -y curl

# Set the default command when container runs
CMD ["echo", "I have completed Day-2 assignment"]
