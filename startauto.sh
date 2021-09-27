#!/bin/bash
sudo add-apt-repository ppa:canonical-chromium-builds/stage
/usr/bin/yes | sudo apt update
/usr/bin/yes | sudo apt install chromium-browser
pip3 install selenium
pip3 istall Faker
wget https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && sudo mv chromedriver /usr/local/bin/
wget https://raw.githubusercontent.com/Verus1989/Databricks/main/proxy.json
wget https://raw.githubusercontent.com/Verus1989/Databricks/main/created.py
wget https://raw.githubusercontent.com/Verus1989/Databricks/main/auto.py
python3 created.py
python3 auto.py
