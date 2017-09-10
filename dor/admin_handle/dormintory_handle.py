# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from dor.models import dor


def handle_change_dor_transcation(request):
    if request.method=="POST":
        sno=request.POST['sno']
        dorm_floor_number=request.POST['dorm_floor_number']
        dorm_floor=request.POST['dorm_floor']
        dorm_number = request.POST['dorm_number']
        bed_number=request.POST['bed_number']
        test=dor(dor_no=dorm_floor_number,sno=sno,room_no=dorm_floor+dorm_number,bed_no=bed_number)
        test.save()
    return HttpResponse("<p>数据添加成功！</p>")

def handle_cancel_dor_transcation(request):
    pass


