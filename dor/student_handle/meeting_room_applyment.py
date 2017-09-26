import datetime
import json

from django.http import HttpResponse
from dor.models import MeetingRoom, MeetingRoomApplymentRecord, MeetingRoomOrderTime, Student
from dor.timeEncoder import TimeEncoder


# 申请研讨室
def stu_meeting_room_applyment(request):
    if request.method == 'GET':
        sno = request.GET.get('sno')

        # 判断检测传进来的是否是学生账号，如果管理员端和学生端同时杂一个浏览器上运行，可能会账号干扰或者替换
        if not list(Student.objects.filter(sno=sno).values()):
            return HttpResponse('此账号不是学生账号，请重新登录', content_type='text', charset='utf8')

        meeting_room_no = request.GET.get('meeting_room_no')
        stu_remark = request.GET.get('stu_remark')
        apply_time = datetime.datetime.strptime(request.GET.get('apply_time'), '%Y-%m-%d %H:%M:%S')
        book_date = datetime.datetime.strptime(request.GET.get('book_date', None), '%Y-%m-%d')
        check_cancel_apply = 0
        check_apply_success = 0
        ad_no = request.GET.get('ad_no', None)
        time_no_1 = request.GET.get('time_no_1', None)
        time_no_2 = request.GET.get('time_no_2', None)
        time_no_3 = request.GET.get('time_no_3', None)
        time_no_4 = request.GET.get('time_no_4', None)
        if time_no_2 == 0:
            time_no_2 = None
        if time_no_3 == 0:
            time_no_3 = None
        if time_no_4 == 0:
            time_no_4 = None
        print(time_no_1)
        print(time_no_2)
        print(time_no_3)
        print(time_no_4)
        obj = MeetingRoomApplymentRecord.objects
        b1 = list(obj.filter(book_date=book_date, time_no_1=time_no_1).values())
        b2 = list(obj.filter(book_date=book_date, time_no_2=time_no_1).values())
        b3 = list(obj.filter(book_date=book_date, time_no_3=time_no_1).values())
        b4 = list(obj.filter(book_date=book_date, time_no_4=time_no_1).values())
        print(b1)
        print(b2)

        b5 = []
        b6 = []
        b7 = []
        b8 = []
        b9 = []
        b10 = []
        b11 = []
        b12 = []
        b13 = []
        b14 = []
        b15 = []
        b16 = []
        if time_no_2 is not None:
            b5 = list(obj.filter(book_date=book_date, time_no_1=time_no_2).values())
            b6 = list(obj.filter(book_date=book_date, time_no_2=time_no_2).values())
            b7 = list(obj.filter(book_date=book_date, time_no_3=time_no_2).values())
            b8 = list(obj.filter(book_date=book_date, time_no_4=time_no_2).values())

        if time_no_3 is not None:
            b9 = list(obj.filter(book_date=book_date, time_no_1=time_no_3).values())
            b10 = list(obj.filter(book_date=book_date, time_no_2=time_no_3).values())
            b11 = list(obj.filter(book_date=book_date, time_no_3=time_no_3).values())
            b12 = list(obj.filter(book_date=book_date, time_no_4=time_no_3).values())

        if time_no_4 is not None:
            b13 = list(obj.filter(book_date=book_date, time_no_1=time_no_4).values())
            b14 = list(obj.filter(book_date=book_date, time_no_2=time_no_4).values())
            b15 = list(obj.filter(book_date=book_date, time_no_3=time_no_4).values())
            b16 = list(obj.filter(book_date=book_date, time_no_4=time_no_4).values())

        for i in (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16):
            if i:
                return HttpResponse('研讨室申请不成功，该时间研讨室已被申请', content_type='text', charset='utf8')

        new_data = MeetingRoomApplymentRecord(apply_time=apply_time, meeting_room_no=meeting_room_no, sno=sno,
                                              check_cancel_apply=check_cancel_apply, book_date=book_date,
                                              check_apply_success=check_apply_success, ad_no=ad_no, time_no_1=time_no_1,
                                              time_no_2=time_no_2, time_no_3=time_no_3, time_no_4=time_no_4,
                                              stu_remark=stu_remark)
        new_data.save()

        return HttpResponse('研讨室申请完成', content_type='text', charset='utf8')


# 查看研讨室 api
def stu_show_meeting_info(request):
    if 'meeting_room_no' in request.GET:
        # 拿到参数
        meeting_room_no = request.GET.get('meeting_room_no')
        book_date = request.GET.get('book_date')
        book_date = datetime.datetime.strptime(book_date, '%Y-%m-%d')
        oneday = datetime.timedelta(days=1)
        # 过滤出数据,并转化成list
        apply_time_list = list(MeetingRoomApplymentRecord.objects.filter(meeting_room_no=meeting_room_no,
                                                                         book_date=book_date).values())
        apply_time_list2 = list(MeetingRoomApplymentRecord.objects.filter(meeting_room_no=meeting_room_no,
                                                                          book_date=book_date + oneday).values())

        time_list_today = []
        time_list_tomorrow = []
        time_list_all = []

        for i in apply_time_list:
            time_list_today.append(i['time_no_1'])
            if i['time_no_2'] is not None:
                time_list_today.append(i['time_no_2'])
            if i['time_no_3'] is not None:
                time_list_today.append(i['time_no_3'])
            if i['time_no_4'] is not None:
                time_list_today.append(i['time_no_4'])
        # 转换成int类型的list
        for j in range(0, len(time_list_today)):
            time_list_today[j] = int(time_list_today[j])
        time_list_today.sort()
        time_list_all.append(time_list_today)

        for i in apply_time_list2:
            time_list_tomorrow.append(i['time_no_1'])
            if i['time_no_2'] is not None:
                time_list_tomorrow.append(i['time_no_2'])
            if i['time_no_3'] is not None:
                time_list_tomorrow.append(i['time_no_3'])
            if i['time_no_4'] is not None:
                time_list_tomorrow.append(i['time_no_4'])
        # 转换成int类型的list
        for j in range(0, len(time_list_tomorrow)):
            time_list_tomorrow[j] = int(time_list_tomorrow[j])
        time_list_tomorrow.sort()
        time_list_all.append(time_list_tomorrow)

        # 注意 要返回的是json格式，否则前端success里接收不到
        time_list_all = json.dumps(time_list_all)

        return HttpResponse(time_list_all, content_type="application/json", charset="utf8")
