# -*- coding: utf-8 -*-
import os
import sys
import time
import django 
#from cdm_data.models import *
sys.path.append("/data/lewzylu/CDM")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CDM.settings")# project_name 项目名称
django.setup()

from django.contrib.auth.models import User

def get_space_data(path):
	total_space = os.popen("df "+path+" | grep "+path+" | awk '{print $2}'").read().split('\n')[0]
	used_space = os.popen("df "+path+" | grep "+path+" | awk '{print $3}'").read().split('\n')[0]
	return used_space,total_space

def get_cpu_net_mem():
	f = os.popen('sh get_cpu_net_mem.sh')
	rt = f.read().split('\n')
	cpu = rt[0]
	net = rt[1]
	mem = rt[2]
	return cpu,net,mem

while(True):	
	t = int(time.time())
	time.sleep(0.5)
	if t % 60 == 0:
		used_space, total_space =  get_space_data('/dev')			
		cpu, net, mem = get_cpu_net_mem()	
		print cpu,net,mem	
#print get_netwidth()

