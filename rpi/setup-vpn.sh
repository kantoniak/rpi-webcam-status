#!/bin/sh

CRED_FILE="/etc/openvpn/credentials"

apt-get install -y openvpn

read -p "Username:" username
read -s -p "Password:" password

touch "${CRED_FILE}"
printf '%s\n' "${username}" "${password}" > "${CRED_FILE}"
