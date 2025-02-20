#!/bin/bash

# Function to display help message
display_help() {
  echo "Usage: $0 [IMAGE_SIZE] [BASE_NAME]"
  echo
  echo "Arguments:"
  echo "  IMAGE_SIZE   Size of the image in GB (default: 15)"
  echo "  BASE_NAME    Base name for the image file (optional)"
  echo
  echo "Options:"
  echo "  --help       Display this help message and exit"
  exit 0
}

# Check for --help option
if [[ "$1" == "--help" ]]; then
  display_help
fi

# Set default values for size and image name
IMAGE_SIZE=${1:-15}
BASE_NAME=$2

# Function to validate the image size
validate_size() {
  if ! [[ "$IMAGE_SIZE" =~ ^[0-9]+$ ]] || [ "$IMAGE_SIZE" -le 0 ]; then
    echo "Invalid size. Please provide a valid positive integer for the size in GB."
    exit 1
  fi
}

# Function to set the base name if not provided
set_base_name() {
  if [ -z "$BASE_NAME" ]; then
    BASE_NAME="disk_image_${IMAGE_SIZE}GB"
  fi
}

# Function to generate a unique image name
generate_image_name() {
  IMAGE_EXTENSION="img"
  INDEX=1
  while [ -f "${BASE_NAME}${INDEX}.${IMAGE_EXTENSION}" ]; do
    INDEX=$((INDEX + 1))
  done
  if [ "$INDEX" -eq 1 ]; then
    IMAGE_NAME="${BASE_NAME}.${IMAGE_EXTENSION}"
  else
    IMAGE_NAME="${BASE_NAME}${INDEX}.${IMAGE_EXTENSION}"
  fi
}

# Function to create the disk image
create_disk_image() {
  qemu-img create -f qcow2 "$IMAGE_NAME" "${IMAGE_SIZE}G"
  echo "Disk image created: $IMAGE_NAME with size ${IMAGE_SIZE}GB"
}

# Main script execution
validate_size
set_base_name
generate_image_name
create_disk_image
