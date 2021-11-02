scp ../scripts.yaml root@192.168.4.139:/root/config/scripts.yaml
scp ../custom_sensors.yaml root@192.168.4.139:/root/config/custom_sensors.yaml
scp ../custom_lights.yaml root@192.168.4.139:/root/config/custom_lights.yaml
scp ../configuration.yaml root@192.168.4.139:/root/config/configuration.yaml
scp ../secrets.yaml root@192.168.4.139:/root/config/secrets.yaml
scp ../groups.yaml root@192.168.4.139:/root/config/groups.yaml
scp ../ui-lovelace.yaml root@192.168.4.139:/root/config/ui-lovelace.yaml
scp -r ../automations/* root@192.168.4.139:/root/config/automations/
scp -r ../input_booleans/* root@192.168.4.139:/root/config/input_booleans/
scp -r ../dashboards/* root@192.168.4.139:/root/config/dashboards/
scp -r ../scenes/* root@192.168.4.139:/root/config/scenes/
