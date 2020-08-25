#!/bin/sh

apt-get install -y python3 pipenv

# Set longer timeout and install dependencies
export PIPENV_TIMEOUT=500
pipenv install

# Enter shell
pipenv shell
