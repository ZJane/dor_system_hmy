# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=20)


bool_value=(('T','true'),('F','false'))

class Stu(models.Model):
    student=models.CharField(max_length=20)

#建立各种表
class student(models.Model):

    gender_choices=(('M','male'),('F','female'))

    sno=models.CharField(max_length=10,primary_key=True)
    sname=models.CharField(max_length=20)
    college_no=models.CharField(max_length=20)
    major_no=models.CharField(max_length=20)
    grade=models.CharField(max_length=10)
    gender=models.CharField(max_length=1,choices=gender_choices)
    dor_no=models.CharField(max_length=10)
    room_no=models.CharField(max_length=10)
    mobilephone=models.CharField(max_length=11)
    email=models.CharField(max_length=40)

class dormintory(models.Model):
    dor_no=models.CharField(max_length=10,primary_key=True)
    dor_name=models.CharField(max_length=20)
    dor_description=models.CharField(max_length=100)

class room(models.Model):
    room_no=models.CharField(max_length=10,primary_key=True)
    dor_no=models.CharField(max_length=10)
    bed_counts=models.IntegerField()
    room_description=models.CharField(max_length=100)
    empty_beds=models.IntegerField()

class dor_applyment(models.Model):
    sno=models.CharField(max_length=10)
    sname=models.CharField(max_length=20)
    dor_no=models.CharField(max_length=10)
    room_no=models.CharField(max_length=10)
    apply_time=models.DateTimeField()
    class Meta:
        unique_together=("sno","dor_no","room_no")


class dor_change(models.Model):
    sno=models.CharField(max_length=10)
    sname=models.CharField(max_length=20)
    old_dor_no=models.CharField(max_length=10)
    old_room_no=models.CharField(max_length=10)
    new_dor_no=models.CharField(max_length=10)
    new_room_no=models.CharField(max_length=10)
    apply_time=models.DateTimeField()
    class Meta:
        unique_together=("sno","old_dor_no","old_room_no")

class dor_cancel(models.Model):
    sno=models.CharField(max_length=10)
    sname=models.CharField(max_length=20)
    dor_no=models.CharField(max_length=10)
    room_no=models.CharField(max_length=10)
    apply_time=models.DateTimeField()
    class Meta:
        unique_together=("sno","dor_no","room_no")

class device(models.Model):
    device_no=models.CharField(max_length=10,primary_key=True)
    device_name=models.CharField(max_length=10)
    device_description=models.CharField(max_length=100)
    device_amount=models.IntegerField()
    device_applied_amount=models.IntegerField()

class organization(models.Model):
    organization_no=models.CharField(max_length=10,primary_key=True)
    organization_name=models.CharField(max_length=20)
    organization_description=models.CharField(max_length=100)

class activity(models.Model):
    activity_no=models.CharField(max_length=10,primary_key=True)
    activity_name=models.CharField(max_length=20)
    organization_no=models.CharField(max_length=10)
    activity_description=models.CharField(max_length=100)
    activity_time=models.DateTimeField()
    activity_num_of_participate=models.IntegerField()
    last_apply_time=models.DateTimeField()

class dor(models.Model):
    dor_no=models.CharField(max_length=10)
    sno=models.CharField(max_length=10)
    room_no=models.CharField(max_length=10)
    bed_no=models.CharField(max_length=10)

class live_on_vacation(models.Model):
    sno=models.CharField(max_length=10,primary_key=True)
    dor_no=models.CharField(max_length=10)
    from_time=models.DateTimeField()
    end_time=models.DateTimeField()
    is_apply_cancel=models.CharField(max_length=1,choices=bool_value)
    is_apply_success=models.CharField(max_length=1,choices=bool_value)
    ad_no=models.CharField(max_length=10)

class activity_applyment(models.Model):
    sno=models.CharField(max_length=10,primary_key=True)
    activity_no=models.CharField(max_length=10)
    is_apply_cancel=models.CharField(max_length=1,choices=bool_value)
    is_apply_success=models.CharField(max_length=1,choices=bool_value)
    apply_time=models.DateTimeField()
    ad_no=models.CharField(max_length=10)

class device_applyment(models.Model):
    sno=models.CharField(max_length=10,primary_key=True)
    device_no=models.CharField(max_length=10)
    from_time=models.DateTimeField()
    dor_no=models.CharField(max_length=10)
    is_apply_cancel=models.CharField(max_length=1,choices=bool_value)
    is_apply_success=models.CharField(max_length=1,choices=bool_value)
    return_device_time=models.DateTimeField()
    ad_no=models.CharField(max_length=10)

class bill(models.Model):
    sno=models.CharField(max_length=10)
    bill_no=models.CharField(max_length=10,primary_key=True)
    item=models.CharField(max_length=20)
    fee=models.FloatField()
    time=models.CharField(max_length=50)


class pay_bill(models.Model):
    sno=models.CharField(max_length=10)
    bill_no=models.CharField(max_length=10)
    is_paied=models.CharField(max_length=1,choices=bool_value)
    pay_time=models.DateTimeField()
    dor_no=models.CharField(max_length=10)
    class Meta:
        unique_together=("sno","bill_no","is_paied")

class repair_device(models.Model):
    sno=models.CharField(max_length=10)
    dor_no=models.CharField(max_length=10)
    room_no=models.CharField(max_length=10)
    mobilephone=models.CharField(max_length=11)
    description=models.CharField(max_length=100)
    apply_time=models.DateTimeField()
    ad_no=models.CharField(max_length=10)
    class Meta:
        unique_together=("sno","apply_time")

class book(models.Model):
    book_no=models.CharField(max_length=10,primary_key=True)
    from_student=models.CharField(max_length=10)
    book_description=models.CharField(max_length=10)
    book_class=models.CharField(max_length=20)
    is_borrowed=models.CharField(max_length=1,choices=bool_value)

class book_applyment(models.Model):
    book_no=models.CharField(max_length=10)
    sno=models.CharField(max_length=10)
    is_apply_cancel=models.CharField(max_length=1,choices=bool_value)
    is_apply_success=models.CharField(max_length=1,choices=bool_value)
    apply_time=models.DateTimeField()
    ad_no=models.CharField(max_length=10)
    class Meta:
        unique_together=("book_no","sno","apply_time")

class meeting_room(models.Model):
    meeting_room_no=models.CharField(max_length=10,primary_key=True)
    meeting_room_size=models.CharField(max_length=10)
    medium=models.CharField(max_length=1,choices=bool_value)
    meeting_room_description=models.CharField(max_length=20)
    is_occupied=models.CharField(max_length=1,choices=bool_value)

class meeting_room_applyment(models.Model):
    meeting_room_no=models.CharField(max_length=10)
    sno=models.CharField(max_length=10)
    is_apply_cancel=models.CharField(max_length=1,choices=bool_value)
    is_apply_success=models.CharField(max_length=1,choices=bool_value)
    apply_time=models.DateTimeField()
    ad_no=models.CharField(max_length=10)
    class Meta:
        unique_together=("meeting_room_no","sno","apply_time")

class meeting_room_time_quantunum(models.Model):
    meeting_room_time_quantunum=models.CharField(max_length=10,primary_key=True)
    from_time=models.DateTimeField()
    end_time=models.DateTimeField()

class adminstrator(models.Model):
    adminstrator_no=models.CharField(max_length=10,primary_key=True)
    adminstrator_name=models.CharField(max_length=20)
    adminstrator_phone=models.CharField(max_length=11)
    dor_no=models.CharField(max_length=10)

class vacation_time_quantum(models.Model):
    vacation_time_quantunum=models.CharField(max_length=10,primary_key=True)
    from_time=models.DateTimeField()
    end_time=models.DateTimeField()

class routine_applyments(models.Model):
    apply_time=models.DateTimeField()
    sno=models.CharField(max_length=10)
    dor_no=models.CharField(max_length=10)
    room_no=models.CharField(max_length=10)
    bed_no=models.CharField(max_length=10)
    apply_content=models.CharField(max_length=100)
    ad_no=models.CharField(max_length=10)
    apply_status=models.CharField(max_length=20)
    detail=models.CharField(max_length=200)
    class Meta:
        unique_together=("sno","apply_time")


