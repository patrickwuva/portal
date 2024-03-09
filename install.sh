#!/bin/sh

mkdir -p "$HOME/.portal"

python3 -m venv "$HOME/.portal/venv"


cp portal.sh /usr/local/bin/portal

chmod +x /usr/local/bin/portal

mv portal.py "$HOME/.portal"
mv helpers "$HOME/.portal"
mv requirements.txt "$HOME/.portal"

cd "$HOME/.portal"

source venv/bin/activate

pip install -r requirements.txt

deactivate

echo "done installing"
