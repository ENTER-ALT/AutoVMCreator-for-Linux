#!/bin/bash

# Set default values for size and image name
IMAGE_SIZE=${1:-15}
IMAGE_NAME=$2

# Check if the provided size is a valid positive number
if ! [[ "$IMAGE_SIZE" =~ ^[0-9]+$ ]] || [ "$IMAGE_SIZE" -le 0 ]; then
  echo "Invalid size. Please provide a valid positive integer for the size in GB."
  exit 1
fi

if [ -z "$IMAGE_NAME" ]; then
  BASE_NAME="disk_image_${IMAGE_SIZE}GB"
  EXTENSION="img"
  INDEX=1
  while [ -f "${BASE_NAME}${INDEX}.${EXTENSION}" ]; do
    INDEX=$((INDEX + 1))
  done
  IMAGE_NAME="${BASE_NAME}${INDEX}.${EXTENSION}"
fi


# Create the disk image using qemu-img
qemu-img create -f qcow2 "$IMAGE_NAME" "${IMAGE_SIZE}G"

echo "Disk image created: $IMAGE_NAME with size ${IMAGE_SIZE}GB"
