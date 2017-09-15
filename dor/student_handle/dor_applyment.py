import pymysql
from django.http import HttpResponse
from django.shortcuts import render
from dor.models import DorChange,DorCheckOut,StudentStayingRecord

def show_change_dor_applyments(request):
    if request.method=='POST':
        key=request.POST.get('apply_sno',None)
    return HttpResponse("<p>"+str(key)+"</p>")

def change_dor_applyment(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        sname=request.POST.get('sname',None)
        old_dor_info=request.POST.get('old_dor_info',None)
        old_dor_info=old_dor_info.split('-')
        apply_time=request.POST.get('apply_time',None)
        new_dor_info=request.POST.get('new_dor_info',None)
        phone=request.POST.get('phone',None)
        reason=request.POST.get('reason',None)
        new_dor_info=new_dor_info.split('-')
        test=DorChange(sno=sno,sname=sname,old_dor_no=old_dor_info[0],old_room_no=old_dor_info[1],new_dor_no=new_dor_info[0],new_room_no=new_dor_info[1]+new_dor_info[2],apply_time=apply_time,phone=phone,reason=reason)
        test.save()

    return HttpResponse('<p>change success</p>')
def show_cancel_dor_applyments(request):
    pass
def cancel_dor_applyment(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        sname=request.POST.get('sname',None)
        dor_info=request.POST.get('dor_info',None)
        dor_info=dor_info.split('-')
        apply_time=request.POST.get('apply_time',None)
        phone=request.POST.get('phone',None)
        reason=request.POST.get('reason',None)
        test=DorCheckOut(sno=sno,sname=sname,dor_no=dor_info[0],room_no=dor_info[1],apply_time=apply_time,phone=phone,reason=reason)
        test.save()
    return HttpResponse('<p>cancel success</p>')

def show_live_on_vacation_applyments(request):
    if request.method=='POST':
        list=StudentStayingRecord.objects.filter(sno='2014101023')
    return render(request, "student/index.html", {'valist': list})

def live_on_vacation_applyment(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        sname=request.POST.get('sname',None)
        test=live_on_vacation_applyment(sno=sno,sname=sname,from_time='2017-07-01',end_time='2017-09-01')
        test.save()
    return HttpResponse('<p>live on vacation success</p>')
