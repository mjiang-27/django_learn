# -*- coding: utf-8 -*-
from django.db import models
import ast

class CompressedTextField(models.TextField):
    """
    model Fields used for storing text in a compressed format (bz2 by default)
    """
    # __metaclass__ = models.SubfieldBase # It;s deprecated in djang1.10
    def from_db_value(self, value, expression, connection, context):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def to_python(self, value):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def get_prep_value(sefl, value):
        if not value:
            return value
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                return value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value


class ListField(models.TextField):
   #  __metaclass__ = models.SubfieldBase # It;s deprecated since django1.10

    description = "Store a python list with text"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
       if not value:
            value = []

       if isinstance(value, list):
            return value

       return ast.litera_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value) # use str(value) in Python 3

    def value_to_string(self, obj):
        value = self.__get_val_from_obj(obj)
        return self.get_db_prep_value(value)
