#!/bin/bash
sudo add-apt-repository ppa:canonical-chromium-builds/stage
/usr/bin/yes | sudo apt update
/usr/bin/yes | sudo apt install chromium-browser
wget https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && sudo mv chromedriver /usr/local/bin/
pip install --upgrade pip
pip install sockets
pip install selenium
pip install Faker
pip install decode
