# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=20)


class Stu(models.Model):
    student=models.CharField(max_length=20)
'''
#建立各种表
class student(models.Model):

    gender_choices=(('M','male'),('F','female'))

    sno=models.CharField(max_length=10,primary_key=True)
    sname=models.CharField(max_length=20)
    college_no=models.CharField(max_length=20)
    major_no=models.CharField(max_length=20)
    grade=models.CharField(max_length=10)
    gender=models.CharField(max_length=1,choices=gender_choices)
    dor_no=models.CharField(max_length=10)
    room_no=models.CharField(max_length=10)
    mobilephone=models.CharField(max_length=11)
    email=models.CharField(max_length=40)
'''



