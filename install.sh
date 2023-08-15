#!/bin/bash

if (( $EUID != 0 )); then
    echo "Please run as root";
    exit;
fi

echo "AnonGT Installer";

sudo apt update;
sudo apt install -y tor iptables bleachbit nyx xterm python3 python3-pip;
sudo mv ../AnonGT /usr/share/anongt;
sudo touch anongt /usr/bin;
sudo echo 'python3 /usr/share/anongt/anongt.py $1' > /usr/bin/anongt;
sudo chmod +x /usr/share/anongt/anongt.py;
sudo chmod +x /usr/bin/anongt;

sudo pip3 install netifaces termcolor;

exit;
