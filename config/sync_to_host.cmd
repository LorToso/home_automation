scp -o MACs=hmac-sha2-512-etm@openssh.com -r ../appdaemon/apps/* lorenzo@192.168.178.26:/root/config/appdaemon/apps/
scp -o MACs=hmac-sha2-512-etm@openssh.com ../appdaemon/appdaemon.yaml lorenzo@192.168.178.26:/root/config/appdaemon/appdaemon.yaml
scp -o MACs=hmac-sha2-512-etm@openssh.com ../secrets.yaml lorenzo@192.168.178.26:/root/config/secrets.yaml