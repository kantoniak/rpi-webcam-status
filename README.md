# Webcam status indicator

## Troubleshooting VPN connection

### Reading saved credentials

Modify OPVN option to read creds from file, e.g.:
```
auth-user-pass /etc/openvpn/credentials
```

### DNS not resolving names

Add options to OPVN, so it will update resolver:
```
script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf
```
