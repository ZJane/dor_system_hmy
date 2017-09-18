from django.http import HttpResponse
from django.shortcuts import render
from dor.models import Activity,ActvityApplyment
def ad_show_activity_applyments(request):
    pass




def ad_handle_activity_applyments(request):
    if request.method == 'POST':
        status = request.POST.get('agree', "不同意申请")
        sno = request.POST.get('sno', None)
        if (sno!=None):
            if (status == "同意申请"):
                ActvityApplyment.objects.filter(sno=sno).update(apply_status="申请成功")
            else:
                ActvityApplyment.objects.filter(sno=sno).update(apply_status="申请失败")
        return HttpResponse("活动申请处理完成")


def ad_show_activity_info(request):
    pass

def ad_new_activity(request):
    if request.method=='POST':
        activity_no=request.POST.get('activity_no',None)
        activiry_name=request.POST.get('activity_name',None)
        host_no = request.POST.get('host_no', None)
        activity_description = request.POST.get('activity_description', None)
        activity_time = request.POST.get('activity_time', None)
        activity_max_participate = request.POST.get('activity_max_participate', None)
        last_apply_time = request.POST.get('last_apply_time', None)
        test=Activity(activity_no=activity_no,activity_name=activiry_name,activity_description=activity_description,host_no=host_no,activity_time=activity_time,activity_max_participate=activity_max_participate,last_apply_time=last_apply_time)
        test.save()
        return HttpResponse("<p>添加成功一个新活动</p>")

def handle(request):
    str=''
    if request.method=='POST':
        str=request.POST['la']
        print(str)
        return render(request,"admin/test.html")
