scp -o MACs=hmac-sha2-512-etm@openssh.com -r root@192.168.178.26:/root/config/appdaemon/apps ../appdaemon
scp -o MACs=hmac-sha2-512-etm@openssh.com -r root@192.168.178.26:/root/config/appdaemon/appdaemon.yaml ../appdaemon/appdaemon.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com -r root@192.168.178.26:/root/config/secrets.yaml ../secrets.yaml
