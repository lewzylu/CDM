# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
class CDMResponse(object):
    def __init__(self, code=0, msg="", data=""):
        self._code = code
        self._msg = msg
        self._data = data
        dict = {}
        dict['code'] = code
        dict['message'] = msg
        dict['data'] = data
        self._httpresponse = HttpResponse(json.dumps(dict),content_type="application/json",status=code)