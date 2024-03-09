#!/bin/bash

cd "$HOME/.portal"

source venv/bin/activate

python portal.py "$@"

deactivate
