from django.shortcuts import render
from dor.models import Activity

def show_stu_activity(request):
    data=Activity.objects.all()
    return render(request,"student/activity.html",{'activity':data})
