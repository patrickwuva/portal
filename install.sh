#!/bin/sh
sudo cp -r .portal "$HOME/"

python3 -m venv "$HOME/.portal/venv"

cp portal /usr/local/bin/

sudo chmod +x /usr/local/bin/portal

cd "$HOME/.portal"

source venv/bin/activate

pip install -r requirements.txt

deactivate

echo "done installing"
