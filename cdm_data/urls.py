# -*- coding: utf-8 -*-
from django.conf.urls import url
from cdm_data import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    
#     (r'^accounts/login/$', 'django.contrib.auth.views.login'),
]