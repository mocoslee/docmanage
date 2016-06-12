#coding:utf-8

from os import path
from django.apps import AppConfig



def get_current_app_name(files):
    
    return path.dirname(files).replace('\\','/').split('/')[-1]

class AppVerboseNameConfig(AppConfig):
    
    name = get_current_app_name(__file__)
    verbose_name = u'日志'
    

default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'
