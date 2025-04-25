#!/bin/bash

echo "---"
# Generate random password for ssh
echo "Generate random password for ssh"
PASSWORD=$(openssl rand -base64 12)
# Setup password for root
echo "Setup password for root"
echo "root:$PASSWORD" | chpasswd
# Print ssh password for root
echo "$(date '+%Y-%m-%d %H:%M:%S') Your ssh password for root: $PASSWORD"
echo "---"
# For ssh
/usr/sbin/sshd
# For testing server
exec python3 -m http.server 3000