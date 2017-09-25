from dor.models import *
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse



class Info():
    def __init__(self):
        self.id = 0
        self.sno = 0
        self.sname  =  ''
        self.college  =  ''
        self.major = ''
        self.now = ''
        self.room_no = ''
        self.phone = ''
        self.mail = ''
        self.apply_title = ''
        self.description = ''
        self.remark = ''
        self.repair_time_1 = ''
        self.repair_time_2 = ''
        self.repair_time_3 = ''
        self.status = 0
        self.ad_no = ''
        self.admin_remark = ''



def admin_repair(request):
    userno = request.session.get('userno','')
    username = request.session.get('username','')
    applyments = DorRepairDevice.objects.all()
    apply_list = []
    for l in applyments:
        s = Student.objects.get(sno=l.sno)
        info = Info()
        info.id = l.id
        info.sno = l.sno
        info.sname = s.sname
        info.college = s.college
        info.major = s.major
        info.now = l.now
        info.room_no = s.room_no
        info.phone = s.stu_phone
        info.mail = s.email
        info.apply_title = l.apply_title
        info.description = l.description
        info.remark = l.remark
        info.repair_time_1 = l.repair_time_1
        info.repair_time_2 = l.repair_time_2
        info.repair_time_3 = l.repair_time_3
        info.status = l.status
        info.ad_no = l.ad_no
        info.admin_remark = l.admin_remark
        apply_list.append(info)

    return render(request,"admin/repair.html",{'apply_list':apply_list, 'userno':userno, 'username':username})


def handle_DorRepairDevice_applyments(request,get_id,get_ad_no):
    if request.method == "POST":
        try:
            get_id = int(get_id)
        except ValueError:
            raise Http404()
        TobeHandle = DorRepairDevice.objects.get(id = get_id)
        if request.POST.get("handle") == "0" :
            TobeHandle.status = 1
        else :
            TobeHandle.status = -1
        TobeHandle.ad_no = get_ad_no
        TobeHandle.admin_remark = request.POST.get('admin_remark',None)
        TobeHandle.save()
        print(request.POST.get("handle"))
    return redirect(reverse('admin_repair'), args=[])


