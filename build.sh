#!/usr/bin/env bash
set -e

apt-get update
apt-get install -y wget unzip curl gnupg

# baixar e instalar Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb || true
apt --fix-broken install -y

# obter versão do Chrome (número principal)
CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)

# baixar chromedriver compatível
CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

# limpeza
rm -f google-chrome-stable_current_amd64.deb chromedriver_linux64.zip
