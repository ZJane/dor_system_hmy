#!/usr/bin/python 
# -*- coding:utf-8 -*-
import os,django
from django.conf import settings
from dor.models import Student,DorStuAccount
from django.contrib.auth.hashers import make_password, check_password

def set_password():
    students = Student.objects.all()
    print(students.values())
    for student in students:
         sno = str(student.sno)
         # sno = student.sno
         account = DorStuAccount.objects.filter(sno=sno).update(password =make_password(sno,None,'pbkdf2_sha256') )

         # print(account)
         # account.password = make_password(sno,None,'pbkdf2_sha256')
         # account.update()
