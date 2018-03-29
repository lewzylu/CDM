# -*- coding: utf-8 -*-
from django.conf.urls import url
from cdm_data import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^storagedata$', views.storagedata),
    url(r'^network$', views.network),
    url(r'^log$', views.log),
    url(r'^active$', views.active),
    url(r'^transfer$', views.transfer),    
#     (r'^accounts/login/$', 'django.contrib.auth.views.login'),
]