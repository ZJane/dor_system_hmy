from django.http import HttpResponse
from django.shortcuts import render
from dor.models import Student,DormitorySchedule,Dormitory,DorRoom
from django.db.models import Q
import json

from dor.student_handle.cry_sha256 import set_password


def search_stu(request):
    dorm_floor_number = request.POST.get('dorm_floor_number','')
    if(dorm_floor_number == '至诚'):
        dorm_floor_number = 'J'
    elif(dorm_floor_number == '弘毅'):
        dorm_floor_number = 'K'
    elif(dorm_floor_number == '思源'):
        dorm_floor_number = 'L'
    elif(dorm_floor_number == '知行'):
        dorm_floor_number = 'M'
    dorm_number = request.POST.get('dorm_number', '')
    student_name = request.POST.get('student_name', '')
    students = Student.objects.filter(Q(sname=student_name)|Q(dor_no=dorm_floor_number)|Q(room_no=dorm_number))

    for student in students:
        dorm_floor = Dormitory.objects.get(dor_no = student.dor_no)
        student.dor_no = dorm_floor.dor_name
    return render(request, 'admin/searchInfo.html',{"students":students,"i":1})

def sort_stu_info(request):
    students = Student.objects.filter(gender='男')
    students.order_by('sname')

def show_student_info(request):
    #a = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    #return HttpResponse(json.dumps(a),content_type='application/json')
    # return HttpResponse("zhang minhua df ")
    if('sno' in request.GET):
        student_sno = request.GET.get('sno')
        # 根据学号获得学生对象，并将集合转换成字典
        student = Student.objects.filter(sno=student_sno).values()
        # 返回json字符串
        print(student)
        # 将字典转换成字典序列
        student = list(student)
        # print(student[0])
        student_json = json.dumps(student[0])
        print(student_json)
        return HttpResponse(student_json, content_type="application/json", charset="utf8")

def show_room_info(request):
    if('sno' in request.GET):
        student_sno = request.GET.get('sno')
        # 根据学号获得学生对象，并将集合转换成字典
        # student = Student.objects.filter(sno=student_sno).values()
        student = Student.objects.get(sno=student_sno)
        dor_schedule = DormitorySchedule.objects.get(sno=student_sno)
        # print(dor_schedule.dor_no)
        dor_room = DorRoom.objects.get(room_no=dor_schedule.room_no)
        # print(dor_room.room_no)
        dormtory = Dormitory.objects.get(dor_no=dor_schedule.dor_no)
        # print(dormtory.dor_name)
        # # 返回json字符串
        # print(student)
        # 将字典转换成字典序列
        # student = list(student)
        # print(student[0])
        # student_json = json.dumps(student[0])
        print(student)
        info = {}
        info['sno'] = student.sno
        info['room_no'] = student.room_no
        info['dor_name'] = dormtory.dor_name
        info['bed_no'] = dor_schedule.bed_no
        info['bed_counts'] = dor_room.bed_counts
        info['empty_beds'] = dor_room.empty_beds
        info['room_phone'] = dor_room.room_phone
        info['student_counts'] = dor_room.bed_counts

        info_json = json.dumps(info)
        print(info_json)
        return HttpResponse(info_json, content_type="application/json", charset="utf8")
