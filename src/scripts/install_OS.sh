#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Incorrect number of arguments."
  echo "Usage: $0 <iso-file> <image-file> --ram=[ram]"
  echo "Example: $0 Manjaro.iso my_image.img --ram=2"
  exit 1
fi

ISO_FILE=$1
IMAGE_FILE=$2
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

# Check if the ISO file exists and is a valid file
if [ ! -f "$ISO_FILE" ]; then
  echo "ISO file '$ISO_FILE' not found or not a valid file."
  echo "Usage: $0 <iso-file> <image-file>"
  exit 1
fi

# Check if the image file exists and is a valid file
if [ ! -f "$IMAGE_FILE" ]; then
  echo "Image file '$IMAGE_FILE' not found or not a valid file."
  echo "Usage: $0 <iso-file> <image-file>"
  exit 1
fi

# Run the QEMU command with the provided ISO and image files
qemu-system-x86_64 \
  -enable-kvm \
  -cdrom "$ISO_FILE" \
  -drive file="$IMAGE_FILE" \
  -m "$RAM" \
  -cpu host \
  -vga virtio \
  -display sdl,gl=on
