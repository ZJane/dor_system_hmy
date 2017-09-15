# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from dor.models import DorChange,DorCheckOut,StudentStayingRecord,Student
from dor.database_operation import database_opr
import pymysql
# Create your views here.

from dor.DTO.StuDorLog import StuDorLogModel


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
    change_log_data=DorChange.objects.filter(sno=2014101003)
    dor_change_list = []
    for i in range(0,len(change_log_data)):
        stu_data = Student.objects.get(sno=2014101003)
        test=StuDorLogModel()
        test.sno=change_log_data[i].sno
        test.sname = change_log_data[i].sname
        test.old_room_no =change_log_data[i].old_room_no
        test.new_room_no = change_log_data[i].new_room_no
        test.apply_time = change_log_data[i].apply_time
        test.reason = change_log_data[i].reason
        test.apply_status = change_log_data[i].app_status
        test.email = stu_data.email
        test.stu_phone = stu_data.stu_phone
        test.college = stu_data.college
        test.major = stu_data.major
        dor_change_list.append(test)

    live_on_vacation_list = StudentStayingRecord.objects.all()
    dor_cancel_list = DorCheckOut.objects.all()

    '''
    dor_change_str="select * from student,dor_change where student.sno=dor_change.sno limit 5"
    data=database_opr(dor_change_str)
    dor_change_list=[]
    for i in range(0,len(data)):
        test =StuDorLogModel()
        test.sno=data[i][10]
        test.sname=data[i][11]
        test.college=data[i][2]
        test.major=data[i][3]
        test.old_room_no=data[i][13]
        test.new_room_no=data[i][15]
        test.email=data[i][9]
        test.stu_phone=data[i][18]
        test.apply_time=data[i][16]
        test.reason=data[i][19]
        test.apply_status=data[i][17]
        dor_change_list.append(test)

    live_on_vacation_str="select * from student,staying_on_vacation_applyment where student.sno=staying_on_vacation_applyment.sno limit 5"
    data = database_opr(live_on_vacation_str)
    live_on_vacation_list=[]
    for i in range(0,len(data)):
        test=StuDorLogModel()
        test.sno=data[i][10]
        test.sname=str(data[i][11])
        test.college=data[i][2]
        test.major=data[i][3]
        test.new_dor_no=data[i][12]
        test.stu_phone=data[i][8]
        test.email=data[i][9]
        test.start_time=str(data[i][13])
        test.end_time=str(data[i][14])
        test.apply_time=str(data[i][12])
        test.reason=data[i][19]
        live_on_vacation_list.append(test)

    #live_on_vacation_list=StudentStayingRecord.objects.filter(sno='2014101021')
    #live_on_vacation_list=StudentStayingRecord.objects.all()
    dor_cancel_list=DorCheckOut.objects.all()
    '''
    return render(request, "student/index.html",{'DorChange':dor_change_list,'LiveOnVacation':live_on_vacation_list,'DorCancel':dor_cancel_list})
