from dor.models import *
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse


def repair(request):
    userno = request.session.get('userno','')
    username = request.session.get('username','')
    stu_info = Student.objects.get(sno=userno)
    if request.method == 'POST':
        sno = request.POST.get('sno', None)
        description = request.POST.get('description', None)
        repair_time_1 = request.POST.get('repair_time_1', None)
        repair_time_2 = request.POST.get('repair_time_2', None)
        repair_time_3 = request.POST.get('repair_time_3', None)
        now = request.POST.get('now', None)
        apply_title = request.POST.get('apply_title', None)
        remark = request.POST.get('remark', None)
        repair_apply = DorRepairDevice(sno=sno,description=description,repair_time_1=repair_time_1,repair_time_2=repair_time_2,
                                     repair_time_3=repair_time_3,now=now,apply_title=apply_title,remark=remark,status=0)
        repair_apply.save()
    apply_list = DorRepairDevice.objects.filter(sno=userno)

    return render(request, "student/repair.html", {'apply_list': apply_list ,'stu':stu_info, 'userno':userno, 'username':username})


def show_device_repair_applyments(request,get_id):
    try:
        get_id = int(get_id)
    except ValueError:
        raise Http404()
    TobeShow = DorRepairDevice.objects.get(id = get_id)
    return render(request,"student/show_device_repair_applyments.html",{'TobeShow':TobeShow})



def cancel_device_repair_applyment(request,get_id):
    if request.method == "POST":
        try:
            get_id = int(get_id)
        except ValueError:
            raise Http404()
    TobeDelete = DorRepairDevice.objects.get(id = get_id)
    TobeDelete.delete()
    return redirect(reverse('repair', args=[]))


