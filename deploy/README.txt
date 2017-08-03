After pull the project from git, please make sure that 'uwsgi' and 'supervisor' are installed on your Linux/Unix.
And then append the configurations below for your configration file of 'supervisor'.

[program:deploy]
command=/usr/bin/uwsgi --http :8001 --ini /home/mjiang/django_learn/deploy/uwsgi.ini
directory=/home/mjiang/django_learn/deploy
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true

[NOTES ABOUT CONFIGURATIONS]
1. In order to install all related tools and modules, you can refer the resources below:
 Install and configure for nginx and uwsgi
 a). http://www.runoob.com/linux/nginx-install-setup.html
 b). http://www.runoob.com/django/django-nginx-uwsgi.html
 c). http://code.ziqiangxuetang.com/django/django-nginx-deploy.html

 Packages relate with python and django
 d). https://pypi.python.org/pypi

2. Please do not configure uwsgi for multi-sites at beginning of our projects.
Since some modules for multi-sites may be not installed, which will result in failure in access sites for our projects.

3. When deployed with nginx, please make sure that the configuration for 'sock' is correct(probably 127.0.0.1 is all right)

4. After installing nginx by ourselves, we may need to add it as system service in OS unix/linux. You can refer the site below:
http://blog.csdn.net/qlong_dd/article/details/45342551
