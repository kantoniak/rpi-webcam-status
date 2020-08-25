#!/bin/sh

OVPN_FILE="/home/pi/vpn/Trust.Zone-Poland.ovpn"

# Kill existing processes
sudo killall openvpn
sudo killall noip2

echo "Connecting..."
sudo openvpn --config "${OVPN_FILE}" --daemon

# Give some time to connect
sleep 15

ip=$(curl ifconfig.me)
echo "Connected. Public IP: ${ip}"

echo "Connecting No IP..."
sudo /usr/local/bin/noip2

pipenv run python main.py
