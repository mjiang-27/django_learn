#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Date: 2017/07/22
# @Autor: mjiang
# @Use: to learn how to use context render

from django.conf import setting as original_setting


def settings(req):
    return {'settings': original_settings}

def ip_address(req):
    return {'ip_address': request.META['REMOTE_ADDR']}
