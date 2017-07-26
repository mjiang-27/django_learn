"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^index/$', app_views.index, name='index'),
    url(r'^add/$', app_views.add, name='add'),
    url(r'^list/$', app_views.lists, name='list'),
    url(r'^add_result/$', app_views.add_result, name='add_result'),
]