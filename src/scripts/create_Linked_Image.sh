#!/bin/bash

# Function to check if at least one argument (image file) is provided
check_arguments() {
  if [ "$#" -lt 1 ]; then
    echo "Incorrect number of arguments."
    echo "Usage: $0 <image-file> [linked-image-name]"
    echo "Example: $0 my_image.img my_linked_image.img"
    exit 1
  fi
}

# Function to parse arguments
parse_arguments() {
  IMAGE_FILE=$1
  LINKED_IMAGE=$2
}

# Function to check if the image file exists and is a valid file
check_image_file() {
  if [ ! -f "$IMAGE_FILE" ]; then
    echo "Image file '$IMAGE_FILE' not found or not a valid file."
    exit 1
  fi
}

# Function to generate a unique linked image name if not specified
generate_linked_image_name() {
  if [ -z "$LINKED_IMAGE" ]; then
    BASE_NAME="${IMAGE_FILE%.*}_linked"
    EXTENSION="${IMAGE_FILE##*.}"
    INDEX=1
    while [ -f "${BASE_NAME}${INDEX}.${EXTENSION}" ]; do
      INDEX=$((INDEX + 1))
    done
    LINKED_IMAGE="${BASE_NAME}${INDEX}.${EXTENSION}"
  fi
}

# Function to create the linked image
create_linked_image() {
  qemu-img create -f qcow2 -b "$IMAGE_FILE" -F qcow2 "$LINKED_IMAGE"
  if [ $? -eq 0 ]; then
    echo "Linked image created successfully: $LINKED_IMAGE"
  else
    echo "Failed to create linked image."
    exit 1
  fi
}

# Main script execution
check_arguments "$@"
parse_arguments "$@"
check_image_file
generate_linked_image_name
create_linked_image
