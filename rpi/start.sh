#!/bin/sh

OVPN_FILE="/home/pi/vpn/Trust.Zone-Poland.ovpn"

echo "Connecting..."
sudo openvpn --config "${OVPN_FILE}" --daemon

# Give some time to connect
sleep 15

ip=$(curl ifconfig.me)
echo "Connected. Public IP: ${ip}"

#pipenv run python main.py
