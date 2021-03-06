from django.shortcuts import render


def show_repair_index(request):
    return render(request,"admin/repair.html")

def show_resource_index(request):
    return render(request,"admin/resource.html")

def show_meeting_room_index(request):
    return render(request,"admin/meeting.html")

def show_activity_index(request):
    return render(request,"admin/activity.html")

def show_book_index(request):
    return render(request,"admin/bookManager.html")

def show_search_index(request):
    return render(request,"admin/searchInfo.html")

def show_checkin_index(request):
    return render(request,"admin/checkIn.html")

def show_set_time_index(request):
    return render(request,"admin/extraStayTime.html")