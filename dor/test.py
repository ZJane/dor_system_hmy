from __future__ import unicode_literals
import os,django
# -*- coding: utf-8 -*-
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dor_system.settings")
django.setup()
from django.db import models
from dor.models import live_on_vacation

data=live_on_vacation.objects.all().filter(sno='2014101023')
print(data)


