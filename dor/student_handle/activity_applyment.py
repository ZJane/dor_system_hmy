from django.http import HttpResponse
import  json
from django.shortcuts import render

from dor.models import ActvityApplyment, Student,Activity


def stu_activity_applyment(request):
    if request.method=="POST":
        activity_no = request.POST.get('aact_no')
        thisact=Activity.objects.get(activity_no=activity_no)
        activity_name=thisact.get('activity_name')
        apply_time=request.POST.get('apply_time',None)
        sno = request.session['userno']
        print("aaa=",apply_time)
        ad_no=' '
        apply_status="申请中"
        test1=ActvityApplyment(actvity_no=activity_no,activity_name=activity_name,sno=sno,apply_time=apply_time,ad_no=ad_no,apply_status=apply_status)
        test1.save()
        return render(request,"student/activity.html")

def stu_show_activity_info(request):
    activity_no = request.POST.get('act_no')
    thisact_data = Activity.objects.filter(activity_no=activity_no).values()
    thisact_data=list(thisact_data)
    print(thisact_data[0])
    thisact=json.dumps(thisact_data[0])
    print(thisact)
    return HttpResponse(thisact,content_type="application/json",charset="utf-8")
