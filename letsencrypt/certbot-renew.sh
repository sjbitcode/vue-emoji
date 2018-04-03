#!/usr/bin/env bash

# This script placed in /etc/cron.monthly to run every month.
sudo docker run --rm -it --name certbot \
-v "/docker-volumes/etc/letsencrypt:/etc/letsencrypt" \
-v "/docker-volumes/var/lib/letsencrypt:/var/lib/letsencrypt" \
-v "/docker/letsencrypt-docker-nginx/src/letsencrypt/letsencrypt-site:/data/letsencrypt" \
-v "/docker-volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot renew --quiet