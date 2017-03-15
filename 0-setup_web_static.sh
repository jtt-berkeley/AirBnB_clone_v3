#!/usr/bin/env bash
sudo apt-get install -y nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo 'Test html' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '39 i/location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}/' /etc/nginx/sites-enabled/default
sudo service nginx restart
