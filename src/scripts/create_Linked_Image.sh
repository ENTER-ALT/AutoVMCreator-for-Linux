#!/bin/bash

# Check if at least one argument (image file) is provided
if [ "$#" -lt 1 ]; then
  echo "Incorrect number of arguments."
  echo "Usage: $0 <image-file> [linked-image-name]"
  echo "Example: $0 my_image.img my_linked_image.img"
  exit 1
fi

# Parse arguments
IMAGE_FILE=$1
LINKED_IMAGE=$2

# Check if the image file exists and is a valid file
if [ ! -f "$IMAGE_FILE" ]; then
  echo "Image file '$IMAGE_FILE' not found or not a valid file."
  exit 1
fi

# If linked image name is not specified, generate a unique one
if [ -z "$LINKED_IMAGE" ]; then
  BASE_NAME="${IMAGE_FILE%.*}_linked"
  EXTENSION="${IMAGE_FILE##*.}"
  INDEX=1
  while [ -f "${BASE_NAME}${INDEX}.${EXTENSION}" ]; do
    INDEX=$((INDEX + 1))
  done
  LINKED_IMAGE="${BASE_NAME}${INDEX}.${EXTENSION}"
fi

# Create the linked image
qemu-img create -f qcow2 -b "$IMAGE_FILE" -F qcow2 "$LINKED_IMAGE"

if [ $? -eq 0 ]; then
  echo "Linked image created successfully: $LINKED_IMAGE"
else
  echo "Failed to create linked image."
  exit 1
fi
