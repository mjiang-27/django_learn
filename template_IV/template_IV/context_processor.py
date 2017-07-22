#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings as orig_settings

def settings(req):
    return {'settings': orig_settings}

def ip_address(req):
    return {'ip_address': req.META['REMOTE_ADDR']}

def request(req):
    return {'request': req}
