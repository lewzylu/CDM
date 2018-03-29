#coding:utf-8
from django.db import models

class Storagedata(models.Model):
    """存储数据z
    """
    used_space = models.CharField(max_length=30)
    total_space = models.CharField(max_length=30)
    eq_status = models.CharField(max_length=30)
    disk_status = models.CharField(max_length=30)
    disk_type = models.CharField(max_length=30)
 
class Network(models.Model):
    """网络设置
    """
    interface = models.CharField(max_length=30, primary_key=True)
    interface_type = models.CharField(max_length=30)
    mac = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    subnet_mask = models.CharField(max_length=30)
    gateway = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
 
    def __unicode__(self):
        return self.interface
 
class Active(models.Model):
    """激活密码
    """
    act_key = models.CharField(max_length=30, primary_key=True)
     
class Log(models.Model):
    """日志
    """
    date = models.CharField(max_length=300)
    handlers = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    mis_type = models.CharField(max_length=30)
    mis_data = models.CharField(max_length=300)
#     

class Transfer(models.Model):
    """迁移映射
    """
    bucket = models.CharField(max_length=300, primary_key=True)
    targer_bucket = models.CharField(max_length=300)
    target_region = models.CharField(max_length=300)
    target_path = models.CharField(max_length=300)
#     

