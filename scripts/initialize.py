# -*- coding: utf-8 -*-
import os
import sys
import time
import django
sys.path.append("/data/lewzylu/CDM")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CDM.settings")
django.setup()
from django.contrib.auth.models import User
from cdm_data.models import *
User.objects.all().delete()
User.objects.create(username='admin', password='', email='327874225@qq.com')
Storagedata.objects.all().delete()
Storagedata.objects.create(used_space='1', total_space='1', eq_status='1', disk_status='1', disk_type='1')
Graphdata.objects.all().delete()
for i in range(1440):
	Graphdata.objects.create(id=i, cpu_use="0%", upstream="0", downstream="0", mem_use="0%")
Network.objects.all().delete()
Active.objects.all().delete()
Log.objects.all().delete()
Transfer.objects.all().delete()
