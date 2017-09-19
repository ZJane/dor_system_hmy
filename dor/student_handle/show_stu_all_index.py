from django.shortcuts import render
from dor.models import Activity

def show_stu_activity(request):
    data=Activity.objects.all()
    return render(request,"student/activity.html",{'activity':data})



def show_stu_repair(request):
    return render(request,"student/repair.html")

def show_stu_pay(request):
    return render(request,"student/payment.html")

def show_stu_resource(request):
    return render(request,"student/resource.html")

def show_stu_meeting_room(request):
    return render(request,"student/meeting.html")

def show_stu_book(request):
    return render(request,"student/book.html")