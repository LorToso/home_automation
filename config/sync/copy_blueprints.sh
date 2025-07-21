#!/bin/bash
echo "Copying blueprints to Home Assistant..."
scp -o MACs=hmac-sha2-512-etm@openssh.com -O -r ../../blueprints/* lorenzo@192.168.178.26:/root/config/blueprints/
echo "Blueprints copied successfully"

echo "Note: Blueprints require a full Home Assistant restart to take effect"