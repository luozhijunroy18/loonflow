#！/bin/sh
uwsgi /opt/loonflow/uwsgi.ini
nginx -c /etc/nginx/nginx.conf -g "daemon off;"