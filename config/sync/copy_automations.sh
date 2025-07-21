#!/bin/bash
echo "Copying automations to Home Assistant..."
scp -o MACs=hmac-sha2-512-etm@openssh.com -O -r ../../automations/* lorenzo@192.168.178.26:/root/config/automations/
echo "Automations copied successfully"

echo "Reloading automations in Home Assistant..."
./ha_reload.sh automation