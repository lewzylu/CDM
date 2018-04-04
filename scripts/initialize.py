# -*- coding: utf-8 -*-
import os
import re
import sys
import time
import django
import logging
from copy import deepcopy 
sys.path.append("/data/lewzylu/CDM")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CDM.settings")
django.setup()
from django.contrib.auth.models import User
from cdm_data.models import *
logger = logging.getLogger('django')
def parse_conf(path): 
    try: 
        linux_type_dict = dict() 
        with open(path, 'r') as f: 
            linux_type_list = f.read().strip().split('\n')
    except IOError:
        pass
    else:
        if linux_type_list is not None:
            linux_type_list_to_purge = deepcopy(linux_type_list)
            # linux_type_list_to_purge = linux_type_list[:]  # another implement, sames to deepcopy
            for member in linux_type_list_to_purge:
                if re.search('^#+.*', member) is not None:
                    member_to_purge = member
                    linux_type_list.remove(member_to_purge)
            for member in linux_type_list:
                sub_member = member.split('=')
                linux_type_dict[sub_member[0]] = sub_member[1].strip('"')
    return linux_type_dict
try:
    User.objects.all().delete()
    User.objects.create(username='admin', password='', email='327874225@qq.com')
    Storagedata.objects.all().delete()
    Storagedata.objects.create(used_space='1', total_space='1', eq_status='1', disk_status='1', disk_type='1')
    Graphdata.objects.all().delete()
    for i in range(1440):
        Graphdata.objects.create(id=i, cpu_use="0%", upstream="0", downstream="0", mem_use="0%")
    Network.objects.all().delete()
    for path in ["/etc/sysconfig/network-scripts/ifcfg-eth0", "/etc/sysconfig/network-scripts/ifcfg-eth1"]:
        eth = parse_conf(path)
        for i in ['DEVICE', 'HWADDR' ,'IPADDR', 'NETMASK', 'GATEWAY', 'ONBOOT']:
            if eth.has_key(i) is False:
                eth[i] = ""
        if eth['ONBOOT'] == "yes":
            eth['ONBOOT'] = "1"
        else:
            eth["ONBOOT"] = "0"
        Network.objects.create(interface=eth['DEVICE'], interface_type="0", mac=eth['HWADDR'], ip=eth['IPADDR'], subnet_mask=eth['NETMASK'], gateway=eth['GATEWAY'], status=eth['ONBOOT'])
    Active.objects.all().delete()
    Log.objects.all().delete()
    Transfer.objects.all().delete()
    logger.info("initialization data success")
except Exception,e:
    logger.warn(e)
    logger.warn("initialization data failed")

