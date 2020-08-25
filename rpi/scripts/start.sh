#!/bin/sh

OVPN_FILE="/home/pi/vpn/Trust.Zone-Poland.ovpn"

echo "Connecting..."
sudo openvpn --config "${OVPN_FILE}" --daemon

# Give some time to connect
sleep 15

ip=$(curl ifconfig.me)
echo "Connected. Public IP: ${ip}"

echo "Connecting No IP..."
sudo /usr/local/bin/noip2

#pipenv run python main.py
