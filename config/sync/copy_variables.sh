#!/bin/bash
echo "Copying variables to Home Assistant..."
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../variables/* lorenzo@192.168.178.26:/root/config/variables/
echo "Variables copied successfully"

echo "Note: Variable changes require a Home Assistant restart to take effect"