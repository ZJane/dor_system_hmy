import pymysql
from django.http import HttpResponse
from django.shortcuts import render
from dor.models import DorChange,DorCheckOut,StudentStayingRecord,StayingOnVacationApplyment

def stu_show_change_dor_applyments(request):
    pass

def stu_change_dor_applyment(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        sname=request.POST.get('sname',None)
        old_dor_info=request.POST.get('old_dor_info',None)
        apply_time=request.POST.get('apply_time',None)
        new_dor_info=request.POST.get('new_dor_info',None)
        phone=request.POST.get('phone',None)
        reason=request.POST.get('reason',None)
        new_dor_info=new_dor_info.split('-')
        test=DorChange(sno=sno,sname=sname,old_room_no=old_dor_info,new_dor_no=new_dor_info[0],new_room_no=new_dor_info[1]+new_dor_info[2],apply_time=apply_time,stu_phone=phone,reason=reason)
        test.save()

    return HttpResponse('<p>change success</p>')
def stu_show_cancel_dor_applyments(request):
    pass

def stu_cancel_dor_applyment(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        sname=request.POST.get('sname',None)
        dor_info=request.POST.get('dor_info',None)
        apply_time=request.POST.get('apply_time',None)
        phone=request.POST.get('phone',None)
        reason=request.POST.get('reason',None)
        test=DorCheckOut(sno=sno,sname=sname,room_no=dor_info,apply_time=apply_time,stu_phone=phone,reason=reason)
        test.save()
    return HttpResponse('<p>cancel success</p>')

def stu_show_live_on_vacation_applyments(request):
    pass

def stu_live_on_vacation_applyment(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        sname=request.POST.get('sname',None)
        start_time=request.POST.get('start_time',None)
        end_time=request.POST.get('end_time',None)
        dor_no=request.POST.get('dor_info',None)
        apply_time=request.POST.get('apply_time',None)
        reason=request.POST.get('staying_reason',None)
        test=StayingOnVacationApplyment(sno=sno,sname=sname,start_time=start_time,end_time=end_time,apply_time=apply_time,reason=reason)
        test.save()
    return HttpResponse('<p>live on vacation success</p>')
