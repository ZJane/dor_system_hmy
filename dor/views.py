# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from dor.models import dor_change,dor_cancel,live_on_vacation
from dor.database_operation import database_opr
import pymysql
# Create your views here.
from dor.models import admin_show_dor_change_applyment_log


def show_index(request):
    return render(request,'index.html')

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
    str="select * from dor_student,dor_dor_change where dor_student.sno=dor_dor_change.sno limit 5"
    data=database_opr(str)
    for i in range(0, len(data)):
        test = admin_show_dor_change_applyment_log(sno=data[i][0], sname=data[i][1], college_no=data[i][2],
                                                   major_no=data[i][3], old_dor_no=data[i][6], old_room_no=data[i][7],
                                                   new_dor_no=data[i][15], new_room_no=data[i][16], email=data[i][9],
                                                   phone=data[i][18], apply_time=data[i][17], reason=data[i][19],status=data[i][20])
        test.save()
    dor_change_list=admin_show_dor_change_applyment_log.objects.all()
    live_on_vacation_list=live_on_vacation.objects.all()
    dor_cancel_list=dor_cancel.objects.all()
    return render(request, "student/index.html",{'DorChange':dor_change_list,'LiveOnVacation':live_on_vacation_list,'DorCancel':dor_cancel_list})

