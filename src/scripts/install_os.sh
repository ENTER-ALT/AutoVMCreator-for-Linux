#!/bin/bash

# Function to check the number of arguments
check_arguments() {
  if [ "$#" -le 1 ]; then
    echo "Incorrect number of arguments."
    echo "Usage: $0 <iso-file> <image-file> --ram=[ram]"
    echo "Example: $0 Manjaro.iso my_image.img --ram=2"
    exit 1
  fi
}

# Function to parse the RAM argument
parse_ram_argument() {
  if [[ "$3" == --ram=* ]]; then
    RAM_VALUE="${3#*=}"
    if [[ "$RAM_VALUE" =~ ^[0-9]+$ ]]; then
      RAM="${RAM_VALUE}G"
    else
      echo "Invalid RAM value. It must be a digit."
      exit 1
    fi
  else
    RAM="2G"
  fi
}

# Function to check if the ISO file exists
check_iso_file() {
  if [ ! -f "$ISO_FILE" ]; then
    echo "ISO file '$ISO_FILE' not found or not a valid file."
    echo "Usage: $0 <iso-file> <image-file>"
    exit 1
  fi
}

# Function to check if the image file exists
check_image_file() {
  if [ ! -f "$IMAGE_FILE" ]; then
    echo "Image file '$IMAGE_FILE' not found or not a valid file."
    echo "Usage: $0 <iso-file> <image-file>"
    exit 1
  fi
}

# Function to run the QEMU command
run_qemu() {
  qemu-system-x86_64 \
    -enable-kvm \
    -cdrom "$ISO_FILE" \
    -drive file="$IMAGE_FILE" \
    -m "$RAM" \
    -cpu host \
    -vga virtio \
    -display sdl,gl=on
}

# Main script execution
check_arguments "$@"
ISO_FILE=$1
IMAGE_FILE=$2
parse_ram_argument "$@"
check_iso_file
check_image_file
run_qemu
