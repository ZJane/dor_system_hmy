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

def resource(request):
    userno = request.session.get('userno','')
    username = request.session.get('username','')
    resource_applyments = DorDeviceApplyment.objects.filter(sno=userno)
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
    return render(request,"student/resource.html", {'resource_list':resource_list, 'userno':userno, 'username':username})
