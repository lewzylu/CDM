import os
import sys
import re
import django
from copy import deepcopy
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
eth0 = parse_conf("/etc/sysconfig/network-scripts/ifcfg-eth0")
eth1 = parse_conf("/etc/sysconfig/network-scripts/ifcfg-eth1")
print eth0
