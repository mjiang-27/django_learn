After pull the project from git, please make sure that 'uwsgi' and 'supervisor' are installed on your Linux/Unix.
And then append the configurations below for your configration file of 'supervisor'.

[program:deploy]
command=/usr/bin/uwsgi --http :8001 --ini /home/mjiang/django_learn/deploy/uwsgi.ini
directory=/home/mjiang/django_learn/deploy
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true

