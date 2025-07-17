scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../configuration.yaml lorenzo@192.168.178.26:/root/config/configuration.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../secrets.yaml lorenzo@192.168.178.26:/root/config/secrets.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../groups.yaml lorenzo@192.168.178.26:/root/config/groups.yaml
scp -O -o MACs=hmac-sha2-512-etm@openssh.com ../../ui-lovelace.yaml lorenzo@192.168.178.26:/root/config/ui-lovelace.yaml
