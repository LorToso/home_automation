#!/bin/bash
echo "Copying helpers and templates to Home Assistant..."
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../input_booleans/* lorenzo@192.168.178.26:/root/config/input_booleans/
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../input_texts/* lorenzo@192.168.178.26:/root/config/input_texts/
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../sensors/* lorenzo@192.168.178.26:/root/config/sensors/
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../binary_sensors/* lorenzo@192.168.178.26:/root/config/binary_sensors/
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../counters/* lorenzo@192.168.178.26:/root/config/counters/
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../input_numbers/* lorenzo@192.168.178.26:/root/config/input_numbers/
scp -O -o MACs=hmac-sha2-512-etm@openssh.com -r ../../timers/* lorenzo@192.168.178.26:/root/config/timers/
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_media_players.yaml lorenzo@192.168.178.26:/root/config/custom_media_players.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_binary_sensors.yaml lorenzo@192.168.178.26:/root/config/custom_binary_sensors.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_sensors.yaml lorenzo@192.168.178.26:/root/config/custom_sensors.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_lights.yaml lorenzo@192.168.178.26:/root/config/custom_lights.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_input_selects.yaml lorenzo@192.168.178.26:/root/config/custom_input_selects.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_templates.yaml lorenzo@192.168.178.26:/root/config/custom_templates.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_datetimes.yaml lorenzo@192.168.178.26:/root/config/custom_datetimes.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../groups.yaml lorenzo@192.168.178.26:/root/config/groups.yaml
echo "Helpers and templates copied successfully"

echo "Reloading template entities in Home Assistant..."
./ha_reload.sh template
./ha_reload.sh input_select
./ha_reload.sh binary_sensor