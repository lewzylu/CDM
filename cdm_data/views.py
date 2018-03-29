# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from cdm_data.response import CDMResponse
from django.contrib.auth.models import User
from cdm_data.models import *
from django.contrib import auth
from django import forms
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse 
import logging
import json
logger = logging.getLogger('django')

@csrf_exempt
def login(request):
    if request.method =='POST':
        json_data = json.loads(request.body)
        username = json_data["username"]
        password = json_data["password"]
        logger.info("login request, username: " + username)
        try:
            user = User.objects.get(username=username,password=password)
            if user is not None and user.is_active:
                res_data={}
                res_data['email']=user.email
                auth.login(request, user)
                logger.info("login success, username: " + username)
                return CDMResponse(code=200,msg="",data=res_data)._httpresponse
            else:
                logger.warn("login failure, The username and passwords do not match")
                return CDMResponse(code=403,msg="The username and passwords do not match")._httpresponse
        except Exception:
            logger.error("Internal Server Error")
            return CDMResponse(code=500,msg=u"Internal Server Error")._httpresponse
        
    return HttpResponse("",content_type="application/json",status=404)

@login_required
@csrf_exempt
def logout(request):
    if request.method =='POST':
        auth.logout(request)
        logger.info("logout success")
        return CDMResponse(code=200,msg="")._httpresponse
    return HttpResponse("",content_type="application/json",status=404)

@login_required
@csrf_exempt
def storagedata(request):
    if request.method =='GET':
        try:
            res_data = {}
            storagedata = storagedata.objects.all()[0]
            res_data['totalspace'] = storagedata.totalspace
            res_data['usedspace'] = storagedata.usedspace
            res_data['eq_status'] = storagedata.eq_status
            res_data['disk_status'] = storagedata.disk_status
            res_data['disk_type'] = storagedata.disk_type
            res_data['cpu_use'] = storagedata.status
            res_data['tape_use'] = storagedata.status
            res_data['mem_use'] = storagedata.status
            return CDMResponse(code=200,msg="",data=res_data)._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    return HttpResponse("",content_type="application/json",status=404)


@login_required
@csrf_exempt
def network(request):
    if request.method =='GET':
        try:
            res_data = {}
            networks = Network.objects.all()
            for network in networks:
                res_data['interface'] = network.interface
                res_data['interface_type'] = network.interface_tyep
                res_data['mac'] = network.mac
                res_data['subnet_mask'] = network.subnet_mask
                res_data['gateway'] = network.gateway
                res_data['status'] = network.status
                return CDMResponse(code=200,msg="",data=res_data)._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    elif request.method =='POST':
        try:
            json_data = json.loads(request.body)
            network = Networks.objects.get(interface=json_data["interface"])
            if network:
                network.ip = json_data['ip']
                network.subnet_mask = json_data['subnet_mask']
                network.gateway = json_data['gateway']
                network.save()
                return CDMResponse(code=200,msg="",data="")._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    return HttpResponse("",content_type="application/json",status=404)

@login_required
@csrf_exempt
def log(request):
    if request.method =='GET':
        try:
            res_data = {}
            logs = Log.objects.all()
            for log in logs:
                res_data['date'] = log.date
                res_data['handlers'] = log.handlers
                res_data['status'] = log.status
                res_data['mis_type'] = log.mis_type
                res_data['mis_data'] = log.mis_data
                return CDMResponse(code=200,msg="",data=res_data)._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    return HttpResponse("",content_type="application/json",status=404)

@login_required
@csrf_exempt
def active(request):
    if request.method =='POST':
        json_data = json.loads(request.body)
        password = json_data["password"]
        try:
            active = Active.objects.get(password=password)
            if active:
                return CDMResponse(code=200,msg="",data=res_data)._httpresponse
            else:
                return CDMResponse(code=403,msg="The password do not match")._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    return HttpResponse("",content_type="application/json",status=404)


@login_required
@csrf_exempt
def transfer(request):
    if request.method =='GET':
        try:
            res_data = {}
            transfers = Transfer.objects.all()
            for transfer in transfers:
                res_data['bucket'] = transfer.bucket
                res_date['target_bucket'] = transfer.target_bucket
                res_data['target_region'] = transfer.target_region
                res_data['target_path'] = transfer.target_path
                return CDMResponse(code=200,msg="",data=res_data)._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    elif request.method =='POST':
        try:
            json_data = json.loads(request.body)
            transfer = Transfer.objects.get(bucket=json_data["bucket"])
            if transfer:
                transfer.bucket = json_data['bucket']
                transfer.subnet_mask = json_data['subnet_mask']
                transfer.gateway = json_data['gateway']
                network.save()
                return CDMResponse(code=200,msg="",data="")._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    elif request.method =='DELETE':
        try:
            json_data = json.loads(request.body)
            transfer = Transfer.objects.get(bucket=json_data["bucket"])
            if transfer:
                transfer.delete()
                return CDMResponse(code=204,msg="",data="")._httpresponse
        except Exception:
            return CDMResponse(code=500,msg=u"Internal error")._httpresponse
    return HttpResponse("",content_type="application/json",status=404)
