from django.shortcuts import render

def show_activity_applyments(request):
    pass

def handle_activity_applyments(request):
    pass

def show_activity_info(request):
    pass

def new_activity(request):
    pass

def handle(request):
    str=''
    if request.method=='POST':
        str=request.POST['la']
        print(str)
        return render(request,"admin/test.html")
