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
    stu_data = Student.objects.get(sno=2014101003)
    sno=stu_data.sno
    sname=stu_data.sname
    college=stu_data.college
    major=stu_data.major
    room_no=stu_data.room_no
    email=stu_data.email
    stu_phone=stu_data.stu_phone

#调宿记录
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
        test.ad_name = '张敏华'
        test.stu_phone = stu_data.stu_phone
        test.college = stu_data.college
        test.major = stu_data.major
        dor_change_list.append(test)
#留校记录
    stayingOnVacation_data=StudentStayingRecord.objects.filter(sno=2014101003)
    live_on_vacation_list=[]
    for i in range(0,len(stayingOnVacation_data)):
        stu_data=Student.objects.get(sno=2014101003)
        test=StuDorLogModel()
        test.sno=stayingOnVacation_data[i].sno
        test.sname = stayingOnVacation_data[i].sname
        test.new_room_no = stayingOnVacation_data[i].room_no
        test.apply_time = stayingOnVacation_data[i].apply_time
        test.reason = stayingOnVacation_data[i].reason
        test.apply_status = stayingOnVacation_data[i].apply_status
        test.email = stu_data.email
        test.ad_name='张敏华'
        test.stu_phone = stayingOnVacation_data[i].stu_phone
        test.college = stu_data.college
        test.major = stu_data.major
        live_on_vacation_list.append(test)


    #live_on_vacation_list = StudentStayingRecord.objects.all()
#退宿记录
    dor_checkout_data=DorCheckOut.objects.filter(sno=2014101003)
    dor_cancel_list =[]
    for i in range(0,len(dor_checkout_data)):
        stu_data=Student.objects.get(sno=2014101003)
        test=StuDorLogModel()
        test.sno = dor_checkout_data[i].sno
        test.sname = dor_checkout_data[i].sname
        test.new_room_no = dor_checkout_data[i].room_no
        test.apply_time = dor_checkout_data[i].apply_time
        test.reason = dor_checkout_data[i].reason
        test.apply_status = dor_checkout_data[i].apply_status
        test.email = stu_data.email
        test.ad_name = '张敏华'
        test.stu_phone = dor_checkout_data[i].stu_phone
        test.college = stu_data.college
        test.major = stu_data.major
        dor_cancel_list.append(test)

    return render(request, "student/index.html",{'DorChange':dor_change_list,'LiveOnVacation':live_on_vacation_list,'DorCancel':dor_cancel_list,
                                                 'sno':sno,'sname':sname,'college':college,'major':major,'room_no':room_no,'stu_phone':stu_phone,'email':email})


