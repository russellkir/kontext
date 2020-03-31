#!/bin/bash -e

# Russell Kirmayer 2020

. bin/shared_functions.sh

check_env
setup_venv

echo "*** Updating runtime environment (this can take a minute)"
loading_display "./venv/bin/pip3 install -U -e ."

./venv/bin/context_app
