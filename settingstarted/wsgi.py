# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 00:25:50 2017

@author: Edison Song
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settingstarted.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)