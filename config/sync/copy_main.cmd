scp -o MACs=hmac-sha2-512-etm@openssh.com ../../configuration.yaml root@192.168.178.26:/root/config/configuration.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../secrets.yaml root@192.168.178.26:/root/config/secrets.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../groups.yaml root@192.168.178.26:/root/config/groups.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../../ui-lovelace.yaml root@192.168.178.26:/root/config/ui-lovelace.yaml
