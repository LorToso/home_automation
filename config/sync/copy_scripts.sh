#!/bin/bash
echo "Copying scripts to Home Assistant..."
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../scripts/* lorenzo@192.168.178.26:/root/config/scripts/
echo "Scripts copied successfully"

echo "Reloading scripts in Home Assistant..."
./ha_reload.sh script