#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.utils import timezone

# Create your models here.

class UserDir(models.Model):
    
    name = models.CharField(max_length=64,default="")
    parentid = models.IntegerField(default=0)
    uid = models.IntegerField(default=0)
    gid = models.IntegerField(default=0)
    is_every = models.IntegerField(default=1)
    ctime = models.DateTimeField(default=timezone.now)

    class Meta:
        
        db_table = 'dirsofdocs'


class UserFile(models.Model):
    
    did = models.IntegerField(default=0)
    ftype = models.CharField(max_length=16,default="")
    fname = models.CharField(max_length=64,default="")
    is_recover = models.IntegerField(default=1)
    uid = models.IntegerField(default=0)
    gid = models.IntegerField(default=0)
    ctime = models.DateTimeField(default=timezone.now)

    class Meta:
        
        db_table = 'filesofdocs'


class UserOps(models.Model):
    
    uid = models.IntegerField(default=0)
    user = models.CharField(max_length=32,default="",verbose_name=u"用户")
    optime = models.DateTimeField(default=timezone.now,verbose_name=u"操作时间")
    ops = models.CharField(max_length=16,default="",verbose_name=u"动作")
    target = models.CharField(max_length=64,default="",verbose_name=u"操作对象")

    class Meta:

        db_table = "useroptions"
        verbose_name_plural = u"操作日志"



