#!/bin/bash

HOST_PORT="192.168.0.20:8000"

function update {
    uses=$(lsmod | grep ^uvcvideo | grep -o [0-9]*$)

    status=0
    if (( uses > 0 )); then
        status=2
    elif (( uses == 0 )); then
        status=1
    fi

    curl -d "{\"status\":${status}}" "http://${HOST_PORT}/update"
}

while true
do
    update
    sleep 2
done
