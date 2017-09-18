# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from dor.models import Student,DormitorySchedule,DorChange,DorCheckOut,StayingOnVacationApplyment,StudentStayingRecord
import pymysql

def ad_show_change_dor_applyments(request):
  if request.method=='POST':
      one_sno=request.POST.get('ssssno',None)
      if(one_sno!=None):
          stu_data=Student.objects.get(sno=one_sno)
          dor_data=DorChange.objects.get(sno=one_sno)
          sno = stu_data.sno
          sname = stu_data.sname
          room_no = stu_data.room_no
          email = stu_data.email
          stu_phone = stu_data.stu_phone
          college = stu_data.college
          major = stu_data.major
          new_dor=dor_data.new_room_no
          apply_time=dor_data.apply_time
          reason=dor_data.reason
  return render(request,"admin/index.html",{'c_sno':sno,'c_sname':sname,'c_room_no':room_no,'c_email':email,'c_stu_phone':stu_phone,'c_college':college,'c_major':major,'c_new_dor':new_dor,'c_apply_time':apply_time,'c_reason':reason})


def ad_handle_change_dor_transcation(request):

    if request.method=="POST":
        sno=request.POST.get('sno',None)
        dorm_floor_number=request.POST.get('dorm_floor_number',None)
        dorm_floor=request.POST.get('dorm_floor',None)
        dorm_number = request.POST.get('dorm_number',None)
        bed_number=request.POST.get('bed_number',None)
        DormitorySchedule.objects.filter(sno=sno).update(dor_no=dorm_floor_number,room_no=dorm_floor+dorm_number,bed_no=bed_number)
        Student.objects.filter(sno=sno).update(dor_no=dorm_floor_number,room_no=dorm_floor+dorm_number)
    return HttpResponse("<p>数据添加成功！</p>")

def ad_show_cancel_dor_applyments(request):
    pass

def ad_handle_cancel_dor_transcation(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        status=request.POST.get('agree_or_not',"不同意申请")
        if(status=='同意申请'):
            test1 = DormitorySchedule.objects.get(sno=sno)
            test1.delete()
            DorCheckOut.objects.filter(sno=sno).update(apply_status="申请成功")
        else:
            DorCheckOut.objects.filter(sno=sno).update(apply_status="申请失败")
    return HttpResponse("<p>退宿办理完成</p>")

def ad_show_live_on_vacation_applyments(request):
    pass

def ad_handle_live_on_vacation_transcation(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        status=request.POST.get('agree_or_not',"不同意申请")
        if(status=='同意申请'):
            StayingOnVacationApplyment.objects.filter(sno=sno).update(apply_status="申请成功")
            data = StayingOnVacationApplyment.objects.get(sno=sno)
            stu_data=Student.objects.get(sno=sno)
            test=StudentStayingRecord(sno=data.sno,sname=data.sname,room_no=data.dor_no,stu_phone=stu_data.stu_phone,start_time=data.start_time,end_time=data.end_time,reason=data.reason,apply_time=data.apply_time,apply_status=data.apply_status)
            test.save()
        else:
            StayingOnVacationApplyment.objects.filter(sno=sno).update(apply_status="申请失败")
    return HttpResponse("<p>假期留宿办理完成</p>")



