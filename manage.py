# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:16:42 2017

@author: Edison Song
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settingstarted.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)