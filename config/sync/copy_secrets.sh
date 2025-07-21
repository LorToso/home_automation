#!/bin/bash
echo "Copying secrets.yaml to Home Assistant..."
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../secrets.yaml lorenzo@192.168.178.26:/root/config/secrets.yaml
echo "Secrets copied successfully"

echo "Reloading core configuration in Home Assistant..."
./reload_core.sh
echo "Core configuration reloaded successfully"