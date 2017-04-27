# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 00:25:50 2017

@author: Edison Song
"""

from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

import ubike

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ubike.urls'))
]
