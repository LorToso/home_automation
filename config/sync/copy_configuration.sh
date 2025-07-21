#!/bin/bash
echo "Copying configuration.yaml to Home Assistant..."
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../configuration.yaml lorenzo@192.168.178.26:/root/config/configuration.yaml
echo "Configuration copied successfully"

echo "Reloading core configuration in Home Assistant..."
./reload_core.sh
echo "Core configuration reloaded successfully"