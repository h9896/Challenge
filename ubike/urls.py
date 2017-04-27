# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:59:23 2017

@author: Edison Song
"""

from django.conf.urls import url
from ubike import views

urlpatterns = [
    url(r'^v1/ubike-station/taipei', views.index),
]