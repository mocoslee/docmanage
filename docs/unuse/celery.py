#coding:utf-8
from __future__ import absolute_import
from celery import Celery
from kombu import Queue
import datetime
from django.conf import settings
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coreops.settings')

app =Celery(settings.CELERY_PROJ,broker=settings.CELERY_BROKER,backend=settings.CELERY_BACKEND)	
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
	CELERY_DEFAULT_EXCHANGE_TYPE = 'direct',
	CELERY_DEFAULT_EXCHANGE = 'password_center',
	CELERY_DEFAULT_ROUTING_KEY = 'default',
	CELERY_DEFAULT_QUEUE = 'default',
	CELERY_QUEUES = (    
		Queue('password_center',routing_key='password_center'),
	),
    CELERY_ROUTES = {
        "coreops_user.tasks.password_commit":{"queue":"password_center"},
        "coreops_user.tasks.delete_commit":{"queue":"password_center"},
        "coreops_user.tasks.password_send":{"queue":"password_center"},
    },
	CELERYD_NODES="worker1",
    CELERYBEAT_SCHEDULE = {
        "trainquery":{
            "task":"coreops_user.tasks.password_commit",
            "schedule":datetime.timedelta(seconds=60),
            "args":()
            
        },
        
    }

)
