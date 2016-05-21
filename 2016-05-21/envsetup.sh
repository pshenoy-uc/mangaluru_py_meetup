#!/usr/bin/env bash

sudo apt-get update -y
sudo apt-get install python-pip python-dev nginx -y
# PIP has not -y option :(
yes w | sudo pip install gunicorn flask

HOME=`pwd`
sudo cp $HOME/2016-05-21/appserver.conf /etc/init/appserver.conf
sudo start appserver

sudo rm -rf /etc/nginx/sites-available/default

sudo cp $HOME/2016-05-21/nginx_appserver.conf /etc/nginx/sites-available/default
