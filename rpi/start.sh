#!/bin/sh

OVPN_FILE="/home/pi/vpn/Trust.Zone-Poland.ovpn"

echo "Connecting..."
sudo openvpn --config "${OVPN_FILE}" --daemon

ip=$(curl ifconfig.me)
echo "Connected. Public IP: ${ip}"

#pipenv run python main.py
