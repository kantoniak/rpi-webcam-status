#!/bin/sh

TMP_DIR=$(mktemp -d)

cd "${TMP_DIR}"
wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
tar vzxf noip-duc-linux.tar.gz && rm noip-duc-linux.tar.gz
cd noip-2.1.9-1
sudo make install
