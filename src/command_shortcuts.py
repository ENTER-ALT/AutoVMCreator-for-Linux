import os
# Scripts path
CREATE_IMAGE_SCRIPT = os.path.join(os.path.dirname(__file__), "scripts/create_image.sh")
INSTALL_OS_SCRIPT = os.path.join(os.path.dirname(__file__), "scripts/install_os.sh")
CREATE_LINKED_IMAGES_SCRIPT = os.path.join(os.path.dirname(__file__), "scripts/create_linked_image.sh")
RUN_MAIN_IMAGE_SCRIPT = os.path.join(os.path.dirname(__file__), "scripts/run_vm.sh")
DELETE_VM_SCRIPT = os.path.join(os.path.dirname(__file__), "scripts/delete_vm.sh")

# Install OS and Run VM script shortcuts
RAM_OPTION = " --ram="
SSH_FORWARDING_PORT_OPTION = " --ssh_forwarding_port="
NO_GRAPHIC_OPTION = " --no-graphic"