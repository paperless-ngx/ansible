#!/bin/bash

if [[ "$VIRTUAL_ENV" != "" ]]
then
    echo "Active venv session detected. Please call 'deacticate' first."
    exit 1
fi

rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r ./.github/workflows/requirements.txt -c ./.github/workflows/constraints.txt
ansible-galaxy install --timeout 120 --verbose -r requirements.yml