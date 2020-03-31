#!/bin/bash -e

# Russell Kirmayer 2020

. bin/shared_functions.sh

check_env
setup_venv

echo "*** Installing test requirements"
loading_display "./venv/bin/python -m pip install -U -e .[test]"

echo "*** Running tests"

./venv/bin/python3 -m pytest --cov=context_app -v ./tests
