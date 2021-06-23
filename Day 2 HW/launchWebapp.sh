#!/bin/sh
sudo apt update
sudo apt install python3
sudo apt install python3-flask -y
git clone https://github.com/JP-Louis/DockerVM home/ubuntu/my-app
cd ~/my-app/Day2/
sudo python3 app.py
