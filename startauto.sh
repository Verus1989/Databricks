#!/bin/bash
sudo add-apt-repository ppa:canonical-chromium-builds/stage
/usr/bin/yes | sudo apt -y update
/usr/bin/yes | sudo apt -y install chromium-browser
wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && sudo mv chromedriver /usr/local/bin/
pip install --upgrade pip
pip install sockets
pip install selenium
pip install Faker
pip install decode
wget https://raw.githubusercontent.com/Verus1989/Databricks/main/auto.py
python auto.py
