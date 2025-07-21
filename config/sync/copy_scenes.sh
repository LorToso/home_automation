#!/bin/bash
echo "Copying scenes to Home Assistant..."
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../scenes/* lorenzo@192.168.178.26:/root/config/scenes/
echo "Scenes copied successfully"

echo "Reloading scenes in Home Assistant..."
./ha_reload.sh scene