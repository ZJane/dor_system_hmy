# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from dor.models import dor,student,dor_change
import pymysql

def show_change_dor_applyments(request):
  pass

def handle_change_dor_transcation(request):
    if request.method=="POST":
        sno=request.POST.get('sno',None)
        dorm_floor_number=request.POST.get('dorm_floor_number',None)
        dorm_floor=request.POST.get('dorm_floor',None)
        dorm_number = request.POST.get('dorm_number',None)
        bed_number=request.POST.get('bed_number',None)
        dor.objects.filter(sno=sno).update(dor_no=dorm_floor_number,room_no=dorm_floor+dorm_number,bed_no=bed_number)
        student.objects.filter(sno=sno).update(dor_no=dorm_floor_number,room_no=dorm_floor+dorm_number)
    return HttpResponse("<p>数据添加成功！</p>")

def show_cancel_dor_applyments(request):
    pass

def handle_cancel_dor_transcation(request):
    pass

def show_live_on_vacation_applyments(request):
    pass

def handle_live_on_vacation_transcation(request):
    pass




