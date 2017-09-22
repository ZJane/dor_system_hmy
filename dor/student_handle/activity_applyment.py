from django.http import HttpResponse
from django.shortcuts import render

from dor.models import ActvityApplyment, Student,Activity


def stu_activity_applyment(request):
    activity_no=request.POST.get('act_no')
    thisact=Activity.objects.get(activity_no=activity_no)
    activity_name=thisact.get('activity_name')

    sno=request.session['userno']
    apply_time=request.POST.get('apply_time',None)
    ad_no='张敏华'
    apply_status="申请中"
    test1=ActvityApplyment(actvity_no=activity_no,activity_name=activity_name,sno=sno,apply_time=apply_time,ad_no=ad_no,apply_status=apply_status)
    test1.save()
    return render(request,"student/activity.html")

def stu_show_activity_info(request):
    activity_no = request.POST.get('act_no')
    thisact = Activity.objects.get(activity_no=activity_no)
    res=[]
    res.append(thisact)
    sno = request.session['userno']
    stu_data=Student.objects.filter(sno=sno)
    res.append(stu_data)
    return render(request,"student/activity.html",{'res':res})