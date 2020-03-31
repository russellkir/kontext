#!/bin/bash -e

# Russell Kirmayer 2020

. bin/shared_functions.sh

check_env
setup_venv

echo "*** Updating runtime environment with test and dev packages (this can take a minute)"

loading_display "./venv/bin/pip3 install -U -e .[test,dev]"
