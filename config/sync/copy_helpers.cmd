scp -o MACs=hmac-sha2-512-etm@openssh.com -pr ../../input_booleans/* root@192.168.178.26:/root/config/input_booleans/
scp -o MACs=hmac-sha2-512-etm@openssh.com -pr ../../input_texts/* root@192.168.178.26:/root/config/input_texts/
scp -o MACs=hmac-sha2-512-etm@openssh.com -pr ../../sensors/* root@192.168.178.26:/root/config/sensors/
scp -o MACs=hmac-sha2-512-etm@openssh.com -pr ../../binary_sensors/* root@192.168.178.26:/root/config/binary_sensors/
scp -o MACs=hmac-sha2-512-etm@openssh.com -pr ../../counters/* root@192.168.178.26:/root/config/counters/
scp -o MACs=hmac-sha2-512-etm@openssh.com -pr ../../input_numbers/* root@192.168.178.26:/root/config/input_numbers/
scp -o MACs=hmac-sha2-512-etm@openssh.com -pr ../../timers/* root@192.168.178.26:/root/config/timers/
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_media_players.yaml root@192.168.178.26:/root/config/custom_media_players.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_binary_sensors.yaml root@192.168.178.26:/root/config/custom_binary_sensors.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_sensors.yaml root@192.168.178.26:/root/config/custom_sensors.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_lights.yaml root@192.168.178.26:/root/config/custom_lights.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_input_selects.yaml root@192.168.178.26:/root/config/custom_input_selects.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_templates.yaml root@192.168.178.26:/root/config/custom_templates.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../custom_datetimes.yaml root@192.168.178.26:/root/config/custom_datetimes.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../groups.yaml root@192.168.178.26:/root/config/groups.yaml