#!/bin/bash
echo " This NGINX Is Running on APP ID ->> $APPID" >> /usr/share/nginx/html/index.html
echo "script RAN!!!!!!"
cat /usr/share/nginx/html/index.html
# source: https://stackoverflow.com/questions/49419021/docker-how-to-commit-a-docker-with-a-new-command-with-quotation-signs
# this restarts the nginx
nginx -g "daemon off;"




 