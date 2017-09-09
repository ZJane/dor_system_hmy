from django.shortcuts import render


def handle(request):
    str=''
    if request.method=='POST':
        str=request.POST['la']
        print(str)
        return render(request,"admin/test.html")
