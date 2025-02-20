#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 <base-image-file>"
    echo "Example: $0 my_image.img"
    exit 1
}

# Function to check if an argument is provided
check_argument() {
    if [ "$#" -ne 1 ]; then
        usage
    fi
}

# Function to check if the base image file exists
check_base_image() {
    if [ ! -f "$BASE_IMAGE" ]; then
        echo "Base image '$BASE_IMAGE' not found."
        exit 1
    fi
}

# Function to delete the base image
delete_base_image() {
    rm -f "$BASE_IMAGE"
    if [ $? -eq 0 ]; then
        echo "Deleted base image: $BASE_IMAGE"
    else
        echo "Failed to delete base image: $BASE_IMAGE"
    fi
}

# Function to delete all linked images associated with the base image
delete_linked_images() {
    INDEX=1
    while [ -f "${BASE_NAME}_linked${INDEX}.${EXTENSION}" ]; do
        rm -f "${BASE_NAME}_linked${INDEX}.${EXTENSION}"
        echo "Deleted linked image: ${BASE_NAME}_linked${INDEX}.${EXTENSION}"
        INDEX=$((INDEX + 1))
    done
}

# Function to delete numbered base images (if they exist)
delete_numbered_images() {
    INDEX=1
    while [ -f "${BASE_NAME}${INDEX}.${EXTENSION}" ]; do
        rm -f "${BASE_NAME}${INDEX}.${EXTENSION}"
        echo "Deleted numbered base image: ${BASE_NAME}${INDEX}.${EXTENSION}"
        INDEX=$((INDEX + 1))
    done
}

# Main script execution
main() {
    check_argument "$@"
    BASE_IMAGE=$1
    check_base_image
    BASE_NAME="${BASE_IMAGE%.*}"
    EXTENSION="${BASE_IMAGE##*.}"
    delete_base_image
    delete_linked_images
    delete_numbered_images
    echo "Cleanup completed."
}

main "$@"
