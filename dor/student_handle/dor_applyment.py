from django.http import HttpResponse

from dor.models import dor_change, dor_cancel, live_on_vacation_applyment

def show_change_dor_applyments(request):
    pass
def change_dor_applyment(request):
    if request.method=='POST':
        sno=request.POST['sno']
        sname=request.POST['sname']
        old_dor_info=request.POST['old_dor_info']
        old_dor_info=old_dor_info.split('-')
        apply_time=request.POST['apply_time']
        new_dor_info=request.POST['new_dor_info']
        phone=request.POST['phone']
        reason=request.POST['reason']
        new_dor_info=new_dor_info.split('-')
        test=dor_change(sno=sno,sname=sname,old_dor_no=old_dor_info[0],old_room_no=old_dor_info[1],new_dor_no=new_dor_info[0],new_room_no=new_dor_info[1]+new_dor_info[2],apply_time=apply_time,phone=phone,reason=reason)
        test.save()
    return HttpResponse('<p>change success</p>')
def show_cancel_dor_applyments(request):
    pass
def cancel_dor_applyment(request):
    if request.method=='POST':
        sno=request.POST['sno']
        sname=request.POST['sname']
        dor_info=request.POST['dor_info']
        dor_info=dor_info.split('-')
        apply_time=request.POST['apply_time']
        phone=request.POST['phone']
        reason=request.POST['reason']
        test=dor_cancel(sno=sno,sname=sname,dor_no=dor_info[0],room_no=dor_info[1],apply_time=apply_time,phone=phone,reason=reason)
        test.save()
    return HttpResponse('<p>cancel success</p>')

def show_live_on_vacation_applyments(request):
    pass

def live_on_vacation_applyment(request):
    if request.method=='POST':
        sno=request.POST['sno']
        sname=request.POST['sname']
        test=live_on_vacation_applyment(sno=sno,sname=sname,from_time='2017-07-01',end_time='2017-09-01')
        test.save()
    return HttpResponse('<p>live on vacation success</p>')
