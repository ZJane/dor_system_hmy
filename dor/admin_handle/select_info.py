from django.http import HttpResponse
from django.shortcuts import render

from dor.models import dor_change
def select_dor_change(request):
    if request.method=='GET':
        dor_change_log=dor_change.objects.all();
        dor_change_log=dor_change_log.get(sno='2014101027')
    return HttpResponse("<p>"+dor_change_log.sno+str(dor_change_log.apply_time)+"</p>")