from django.shortcuts import render

from dor.DTO.StuDorLog import PayLogModel
from dor.models import Activity, ActvityApplyment,DorCostRecord, StuPayRecord, Student,DorBookInf


def show_stu_activity(request):
    data=Activity.objects.filter()
    sno = request.session['userno']
    sname=request.session['username']
    test = Student.objects.get(sno=sno)
    activity_log=ActvityApplyment.objects.filter(sno=sno)
    return render(request, "student/activity.html",
                  {'sno':sno,'sname':sname,'activity':data,'sname': test.sname, 'college': test.college, 'major': test.major, 'room_no': test.room_no,
                   'stu_phone': test.stu_phone, 'email': test.email,'activity_log':activity_log})


def show_stu_repair(request):
    sno=request.session['userno']
    sname=request.session['username']
    return render(request,"student/repair.html",{'username':sname,'userno':sno})

def show_stu_pay(request):
    data = DorCostRecord.objects.all()
    pay_list = []
    for i in range(0, len(data)):
        p = PayLogModel()
        test = StuPayRecord.objects.get(bill_no=data[i].cost_no)
        p.cost_no = data[i].cost_no
        p.item = data[i].item
        p.fee = data[i].fee
        p.time = data[i].time
        p.dor_no = test.dor_no
        p.status = test.check_paied
        pay_list.append(p)

    return render(request, "student/payment.html", {'paylog': pay_list})

def show_stu_resource(request):
    sno=request.session['userno']
    sname=request.session['username']
    return render(request,"student/resource.html",{'username':sname,'userno':sno})

def show_stu_meeting_room(request):
    sno = request.session['userno']
    sname = request.session['username']
    return render(request,"student/meeting.html",{'username':sname,'userno':sno})

def show_stu_book(request):
    sno = request.session['userno']
    sname = request.session['username']
    book_list = DorBookInf.objects.all().values()
    book_borrow_list =DorBookInf.objects.filter(book_borrowman=sname)
    book_share_list =DorBookInf.objects.filter(book_share_man="1", book_borrowman=sname)

    return render(request,"student/book.html",{'username':sname,'userno':sno,
                                               'book_list':book_list,
                                                   'book_borrow_list': book_borrow_list,
                                                   'book_share_list':book_share_list})