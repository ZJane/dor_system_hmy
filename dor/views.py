# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from dor.models import Test
# Create your views here.

def show_main(request):
    str="null"
    if 'bb'in request.GET:
        str=request.GET['bb']
    return render(request,"tsst.html",{'data':str})
def show_admin_index(request):
    '''
    str="null"
    if request.method=='POST':
        str=request.POST['aa']
    return render(request,"tsst.html",{'data':str})
    '''
    return render(request,"admin/index.html")

def show_student_index(request):
    return render(request,"student/index.html")