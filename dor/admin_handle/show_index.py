from django.shortcuts import render
from dor.models import DorBookInf


def show_repair_index(request):
    username = request.session['username']
    return render(request,"admin/repair.html",{'username':username})

def show_resource_index(request):
    username = request.session['username']
    return render(request,"admin/resource.html",{'username':username})

def show_meeting_room_index(request):
    username = request.session['username']
    return render(request,"admin/meeting.html",{'username':username})

def show_activity_index(request):
    username=request.session['username']
    return render(request,"admin/activity.html",{'username':username})

def show_book_index(request):
    username = request.session['username']
    book_list = DorBookInf.objects.all().values()
    return render(request, "admin/bookManager.html", {'username':username,'book_list': book_list})

def show_search_index(request):
    username = request.session['username']
    return render(request,"admin/searchInfo.html",{'username':username})

def show_checkin_index(request):
    username = request.session['username']
    return render(request, "admin/checkIn.html", {'username': username})

def show_set_time_index(request):
    username = request.session['username']
    return render(request,"admin/extraStayTime.html",{'username':username})