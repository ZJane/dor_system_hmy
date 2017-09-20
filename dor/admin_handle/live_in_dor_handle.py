from django.shortcuts import render


def ad_add_stu_dor_info(request):
    username=request.session['username']
    return render(request, "admin/checkIn.html",{'username':username})
def ad_distribute_dor(request):
    pass
