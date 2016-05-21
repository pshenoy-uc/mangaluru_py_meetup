#!/usr/bin/env bash

sudo apt-get update -y
sudo apt-get install python-pip python-dev nginx -y
# PIP has not -y option :(
yes w | sudo pip install gunicorn flask

sudo cp /home/codaxtr_user/pydemo/appserver.conf /etc/init/appserver.conf
sudo start appserver

sudo rm -rf /etc/nginx/sites-available/default

sudo cp /home/codaxtr_user/pydemo/nginx_appserver.conf /etc/nginx/sites-available/default