#!/bin/bash

if [[ "$VIRTUAL_ENV" != "" ]]
then
    echo "Active venv session detected. Please call 'deacticate' first."
    exit 1
fi

echo "Deleting existing venv dir ..."
rm -rf .venv
echo "Creating new venv ..."
python3 -m venv .venv
echo "Activating venv ..."
source .venv/bin/activate
echo "Installing deps ..."
python3 -m pip install -r ./.github/workflows/requirements.txt -c ./.github/workflows/constraints.txt
ansible-galaxy install --timeout 120 --verbose -r requirements.yml