#!/bin/bash

# Function to display usage information
usage() {
  echo "Usage: $0 <image-file> [ssh-forwarding-port] [ram] [--no-graphic|-ng] [--help|-h]"
  echo "Example: $0 my_image.img 7000 2 --no-graphic"
  exit 1
}

# Function to check if the image file exists
check_image_file() {
  if [ ! -f "$IMAGE_FILE" ]; then
    echo "Image file '$IMAGE_FILE' not found or not a valid file."
    usage
  fi
}

# Function to find the first available port in range 7000-8000
find_available_port() {
  for PORT in {7000..8000}; do
    if ! ss -tuln | grep -q ":$PORT "; then
      SSH_PORT=$PORT
      break
    fi
  done
  
  if [ -z "$SSH_PORT" ]; then
    echo "No available port found in range 7000-8000."
    exit 1
  fi
  echo "No port specified, using available port: $SSH_PORT"
}

# Function to assign RAM
assign_ram() {
  if [[ "$1" =~ ^[0-9]+$ ]]; then
    RAM="${1}G"
  else
    echo "Invalid RAM value. It must be a digit."
    exit 1
  fi
}

# Function to parse arguments
parse_arguments() {
  IMAGE_FILE=$1
  shift  # Shift to process optional arguments

  while [[ "$#" -gt 0 ]]; do
    case $1 in
      --no-graphic|-ng)
        GRAPHIC_MODE=false
        shift
        ;;
      --help|-h)
        usage
        ;;
      [0-9]*)
        SSH_PORT=$1
        shift
        ;;
      --ram=*)
        assign_ram "${1#*=}"
        shift
        ;;
      *)
        echo "Unknown argument: $1"
        usage
        ;;
    esac
  done
}

# Function to prepare QEMU command options based on graphic mode
prepare_display_option() {
  if [ "$GRAPHIC_MODE" = true ]; then
    DISPLAY_OPTION="-display sdl,gl=on"
  else
    DISPLAY_OPTION="-nographic"
  fi
}

# Function to run the QEMU command
run_qemu() {
  qemu-system-x86_64 \
    -enable-kvm \
    -drive file="$IMAGE_FILE" \
    -m "$RAM" \
    -cpu host \
    -vga virtio \
    -net user,hostfwd=tcp::$SSH_PORT-:22 \
    -net nic \
    $DISPLAY_OPTION
}

# Main script execution
main() {
  # Check if at least one argument (image file) is provided
  if [ "$#" -lt 1 ]; then
    usage
  fi

  # Default values
  SSH_PORT=""
  RAM="2G"
  GRAPHIC_MODE=true

  # Parse arguments
  parse_arguments "$@"

  # Check if the image file exists and is a valid file
  check_image_file

  # If SSH_PORT is not specified, find the first available port in range 7000-8000
  if [ -z "$SSH_PORT" ]; then
    find_available_port
  fi

  # Prepare QEMU command options based on graphic mode
  prepare_display_option

  # Run the QEMU command with the provided image file and SSH forwarding port
  run_qemu
}

# Call the main function with all script arguments
main "$@"
