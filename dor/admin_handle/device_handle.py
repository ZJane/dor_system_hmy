from dor.models import *
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, Http404
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
        self.item = ''
        self.reason = ''
        self.remark = ''
        self.return_time = ''
        self.status = 0
        self.ad_no = ''


#显示借用首页
def admin_resource(request):
    userno = request.session.get('userno','')
    username = request.session.get('username','')
    resource_applyments = DorDeviceApplyment.objects.all()
    resource_list = []
    for l in resource_applyments:
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
        info.item = l.item
        info.reason = l.reason
        info.remark = l.remark
        info.return_time = l.return_time
        info.status = l.status
        info.ad_no = l.ad_no
        resource_list.append(info)
    return render(request, "admin/resource.html",{'resource_list':resource_list, 'userno':userno, 'username':username})


#借用钥匙
def borrow_key_applyments(request):
    if request.method == 'POST':
        sno = request.POST.get('sno',None)
        now = request.POST.get('now',None)
        reason = request.POST.get('reason',None)
        remark = request.POST.get('remark',None)
        key_applyments = DorDeviceApplyment(sno=sno,now=now,reason=reason,remark=remark,item="钥匙",status=1)
        key_applyments.save()
    return redirect(reverse('admin_resource'),args=[])


#借用空调遥控器
def borrow_minitor_applyments(request):
    if request.method == 'POST':
        sno = request.POST.get('sno',None)
        now = request.POST.get('now',None)
        reason = request.POST.get('reason',None)
        remark = request.POST.get('remark',None)
        key_applyments = DorDeviceApplyment(sno=sno,now=now,reason=reason,remark=remark,item="空调遥控器",status=1)
        key_applyments.save()
    return redirect(reverse('admin_resource'),args=[])


def commit_return_device(request,get_id,get_ad_no):
    if request.method == "POST":
        try:
            get_id=int(get_id)
        except ValueError:
            raise Http404
        toreturn = DorDeviceApplyment.objects.get(id=get_id)
        toreturn.status=0
        toreturn.return_time = request.POST.get("return_time",None)
        toreturn.ad_no = get_ad_no
        toreturn.save()
    return redirect(reverse('admin_resource'),args=[])