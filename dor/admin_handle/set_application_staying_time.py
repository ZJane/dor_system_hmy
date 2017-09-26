from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from dor.models import StayingApplyTime

def show_staying_time(request):
    return render(request, 'admin/extraStayTime.html')

def set_staying_time(request):
    staying_time = {}
    staying_time['selected_year'] = request.GET.get('selected_year')
    staying_time['selected_vocation'] = request.GET.get('selected_vocation')
    staying_time['first_start_time'] = request.GET.get('first_start_time')
    staying_time['first_end_time'] = request.GET.get('first_end_time')
    staying_time['second_start_time'] = request.GET.get('second_start_time')
    staying_time['second_end_time'] = request.GET.get('second_end_time')
    print(staying_time)
    vocation = ""
    if(staying_time['selected_vocation']=='寒假'):
        vocation = "winter"
    else:
        vocation = "summer"
    staying_time['first_time_no'] = "%s_%s_first" % (str(staying_time['selected_year']),vocation)
    staying_time['second_time_no'] = "%s_%s_second" % (str(staying_time['selected_year']),vocation)
    print(staying_time['first_time_no'],staying_time['second_time_no'])

    # staying_time['first_time_no'] = "test"
    # staying_time['second_time_no'] = "test_first"

    # 数据库中插入或者更新第一阶段留校时间
    time_first = StayingApplyTime(staying_apply_time_no=staying_time['first_time_no'],
                                                year = staying_time['selected_year'],
                                                vocation = staying_time['selected_vocation'],
                                                start_time= staying_time['first_start_time'],
                                                end_time= staying_time['first_end_time'])
    print(time_first)
    time_first.save()

    # 数据库中插入或者更新第二阶段留校时间
    time_second = StayingApplyTime(staying_apply_time_no=staying_time['second_time_no'],
                                                year = staying_time['selected_year'],
                                                vocation = staying_time['selected_vocation'],
                                                start_time= staying_time['second_start_time'],
                                                end_time= staying_time['second_end_time'])
    print(time_second)
    time_second.save()

    return render(request, 'admin/extraStayTime.html')
    # return HttpResponse(request,'extraStayTime.html',"hello" )