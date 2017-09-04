# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import hashlib

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=60)
    phone = models.CharField(max_length=20,default=None)
    mail = models.EmailField(max_length=50)
    department = models.CharField(max_length=80)
    job = models.CharField(max_length=50)

    def save(self,*args,**kwargs):
        self.password = hashlib.sha1(self.password+self.username+'ylhb').hexdigest()
        super(User,self).save(*args,**kwargs)

    def __unicode__(self):
        return self.username

class Apps(models.Model):
    business_name = models.CharField(max_length=60, primary_key=True)
    app_name = models.CharField(max_length=30,default=None)
    app_server_ip = models.GenericIPAddressField(max_length=30,default=None)
    app_server_port = models.IntegerField(default=None)

    def __unicode__(self):
        return self.business_name

class Roles(models.Model):
    role_name = models.CharField(max_length=30, primary_key=True)
    business_name = models.ForeignKey('Apps', to_field='business_name')
    username = models.ForeignKey('User', to_field='username')

    def __unicode__(self):
        return self.role_name
