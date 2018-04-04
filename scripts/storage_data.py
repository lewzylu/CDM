# -*- coding: utf-8 -*-
import os
import sys
import time
import django 
import logging
sys.path.append("/data/lewzylu/CDM")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CDM.settings")# project_name 项目名称
django.setup()
from cdm_data.models import *
from django.contrib.auth.models import User

logger =  logging.getLogger('django')
def get_space_data(path):
	total_space = os.popen("df "+path+" | grep "+path+" | awk '{print $2}'").read().split('\n')[0]
	used_space = os.popen("df "+path+" | grep "+path+" | awk '{print $3}'").read().split('\n')[0]
	return used_space,total_space

def get_cpu_net_mem():
	f = os.popen('sh get_cpu_net_mem.sh')
	rt = f.read().split('\n')
	cpu = rt[0] + "%"
	upstream = rt[1]
	downstream = rt[2]
	mem = rt[3]
	return cpu, upstream, downstream, mem

while(True):	
	t = int(time.time())
	time.sleep(0.5)
	if t % 1  == 0:
		try:
			t = t/60 % 1440
			used_space, total_space =  get_space_data('/dev')			
			st = Storagedata.objects.all()[0]
			st.used_space = used_space
			st.total_space = total_space
			st.eq_status = '1'
			st.disk_status = 'RAID 5'
			st.disk_type = '1'
			st.save()
			logger.info("used_space: {used_space}, total_space: {total_space}, eq_status: {eq_status}, disk_status: {disk_status}, disk_type: {disk_type}"
			.format(used_space=st.used_space, total_space=st.total_space, eq_status=st.eq_status, disk_status=st.disk_status, disk_type=st.disk_type))
		except:
			logger.warn("get storage_data failed")
		try:
			cpu, upstream, downstream, mem = get_cpu_net_mem()
			gd = Graphdata.objects.get(id = t)
			gd.cpu_use = cpu
			gd.upstream = upstream
			gd.downstream = downstream
			gd.mem_use = mem
			gd.save()
            logger.info("cpu_use: {cpu_use}, upstream: {upstream}, downstream: {downstream}, mem_use: {mem_use}".format(cpu_use=cpu, upstream=upstream, downstream=downstream, mem_use=mem))
		except:
			logger.warn("get cpu_net_memory failed")
#print get_netwidth()

