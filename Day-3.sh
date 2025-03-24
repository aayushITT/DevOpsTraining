#!/bin/bash

grant_file_permissions() {
    local file=$1
    local entity=$2
    if [ -f $file ]; then
        chmod $entity+rw $file
        echo Read and write permissions granted to $entity for file: $file
    else
        echo Error: File $file does not exist.
    fi
}

grant_folder_permissions() {
    local folder=$1
    local entity=$2
    if [ -d $folder ]; then
        chmod $entity+r $folder
        echo Read permission granted to $entity for folder: $folder
    else
        echo Error: Folder $folder does not exist.
    fi
}

echo "Select an option:"
echo "1. Change file permissions to read and write"
echo "2. Change folder permissions to read"
read -p "Enter your choice (1 or 2): " choice

echo "Select to whom you want to give permission:"
echo "u - User"
echo "g - Group"
echo "o - Others"
read -p "Enter your choice (u/g/o): " entity

if [ $choice -eq 1 ]; then
    read -p "Enter the filename: " filename
    grant_file_permissions $filename $entity
elif [ $choice -eq 2 ]; then
    read -p "Enter the folder name: " foldername
    grant_folder_permissions $foldername $entity
else
    echo "Invalid choice. Exiting."
fi