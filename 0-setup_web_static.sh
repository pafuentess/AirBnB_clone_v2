#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
mkdir /data/ 
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '42i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t\n}' /etc/nginx/sites-available/default
sudo service nginx restart

