#!/bin/bash
echo "Copying dashboards and ui-lovelace.yaml to Home Assistant..."
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../dashboards/* lorenzo@192.168.178.26:/root/config/dashboards
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../ui-lovelace.yaml lorenzo@192.168.178.26:/root/config/ui-lovelace.yaml
echo "Dashboards copied successfully"

echo "Note: Dashboard changes will be visible immediately in Home Assistant UI"