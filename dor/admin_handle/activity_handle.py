from django.shortcuts import render

def ad_show_activity_applyments(request):
    pass

def ad_handle_activity_applyments(request):
    pass

def ad_show_activity_info(request):
    pass

def ad_new_activity(request):
    pass

def handle(request):
    str=''
    if request.method=='POST':
        str=request.POST['la']
        print(str)
        return render(request,"admin/test.html")
