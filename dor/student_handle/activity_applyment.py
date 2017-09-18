from django.http import HttpResponse
from dor.models import ActvityApplyment

def stu_activity_applyment(request):
    activity_no=1
    sno=request.POST.get('sno',None)
    apply_time=request.POST.get('apply_time',None)
    ad_no='张敏华'
    apply_status="申请中"
    test=ActvityApplyment(actvity_no=activity_no,sno=sno,apply_time=apply_time,ad_no=ad_no,apply_status=apply_status)
    test.save()
    return HttpResponse("申请成功！")

def stu_show_activity_info(request):
    pass