from django.shortcuts import render


def show_index(request):
    str="null"
    if request.method=='POST':
        str=request.POST['aa']
        return render(request,"tsst.html",{'data':str})