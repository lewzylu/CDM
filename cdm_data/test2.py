# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import requests
import json
s = requests.session()
data= '{"username": "admin", "password": ""}'
print json.loads(data)
rt =s.post("http://127.0.0.1:8000/login",data=data)
# Create your tests here.
print rt.text
 
rt =s.get("http://127.0.0.1:8000/storagedata")
# Create your tests here.
print rt.text
#rt =s.post("http://127.0.0.1:8099/logout")
# Create your tests here.
#print rt.text

#rt =s.post("http://127.0.0.1:8099/logout")
# Create your tests here.
#print rt.text
