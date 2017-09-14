"""dor_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dor.views import show_admin_index,show_student_index,show_index
from dor.admin_handle.select_info import select_dor_change
from dor.admin_handle.dormintory_handle import handle_cancel_dor_transcation,handle_change_dor_transcation,handle_live_on_vacation_transcation,show_cancel_dor_applyments,show_change_dor_applyments,show_live_on_vacation_applyments
from dor.admin_handle.repair_handle import  show_repair_device_applyments,handle_repair_device_applyment
from dor.admin_handle.device_handle import show_device_applyments,show_key_applyments,show_minitor_applyments,commit_return_device
from dor.admin_handle.meeting_room_handle import show_meeting_room_applyments,show_meeting_room_info,handle_meeting_room_applyments
from dor.admin_handle.activity_handle import show_activity_applyments,show_activity_info,handle_activity_applyments,new_activity
from dor.admin_handle.book_handle import new_book,show_books_info
from dor.admin_handle.search_handle import search_stu,show_room_info,sort_stu_info
from dor.admin_handle.live_in_dor_handle import add_stu_dor_info,distribute_dor
from dor.admin_handle.set_timequantum import set_timeable
from dor.student_handle.dor_applyment import change_dor_applyment,cancel_dor_applyment,live_on_vacation_applyment,show_live_on_vacation_applyments,show_cancel_dor_applyments,show_change_dor_applyments
from dor.student_handle.resource_applyment import show_minitor_applyments,show_key_applyments
from dor.student_handle.pay_bill import show_bill,pay_bill
from dor.student_handle.activity_applyment import activity_applyment,show_activity_info
from dor.student_handle.book_applyment import book_applyment,my_borrowed_books,my_shared_books,show_book_info,search_book
from dor.student_handle.meeting_room_applyment import meeting_room_applyment,show_meeting_info
from dor.student_handle.device_repair_applyment import device_repair_applyment,cancel_device_repair_applyment,show_device_repair_applyments
urlpatterns = [
    url(r'^index/',show_index),
    url(r'^admin/',admin.site.urls),
    url(r'^show_admin_index',show_admin_index),
    url(r'^admin/select_dor_change',select_dor_change),
    url(r'^show_student_index',show_student_index),
    url(r'^dor/student_handle/dor_applyment/show_change_dor_applyments',show_change_dor_applyments),
    url(r'^dor/student_handle/dor_applyment/change_dor_applyment',change_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/show_cancel_dor_applyments',show_cancel_dor_applyments),
    url(r'^dor/student_handle/dor_applyment/cancel_dor_applyment',cancel_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/show_live_on_vacation_applyments',show_live_on_vacation_applyments),
    url(r'^dor/student_handle/dor_applyment/live_on_vacation_applyment',live_on_vacation_applyment),
    url(r'^dor/student_handle/device_repair_applyment/device_repair_applyment', device_repair_applyment),
    url(r'^dor/student_handle/device_repair_applyment/show_device_repair_applyments',show_device_repair_applyments),
    url(r'^dor/student_handle/device_repair_applyment/cancel_device_repair_applyment',cancel_device_repair_applyment),
    url(r'^dor/student_handle/resource_applyment/show_minitor_applyments',show_minitor_applyments),
    url(r'^dor/student_handle/resource_applyment/show_key_applyments',show_key_applyments),
    url(r'^dor/student_handle/pay_bill/show_bill',show_bill),
    url(r'^dor/student_handle/pay_bill/pay_bill',pay_bill),
    url(r'^dor/student_handle/activity_applyment/activity_applyment',activity_applyment),
    url(r'^dor/student_handle/activity_applyment/show_activity_info',show_activity_info),
    url(r'^dor/student_handle/meeting_room_applyment/meeting_room_applyment',meeting_room_applyment),
    url(r'^dor/student_handle/meeting_room_applyment/show_meeting_room_info', show_meeting_info),
    url(r'^dor/student_handle/book_applyment/my_shared_books', my_shared_books),
    url(r'^dor/student_handle/book_applyment/book_applyment',book_applyment),
    url(r'^dor/student_handle/book_applyment/my_borrowed_books', my_borrowed_books),
    url(r'^dor/student_handle/book_applyment/search_book',search_book),
    url(r'^dor/student_handle/book_applyment/show_book_info',show_book_info),


    url(r'^dor/admin_handle/dormintory_handle/show_change_dor_applyments', show_change_dor_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_change_dor_transcation',handle_change_dor_transcation),
    url(r'^dor/admin_handle/dormintory_handle/show_cancel_dor_applyments', show_cancel_dor_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_cancel_dor_transcation',handle_cancel_dor_transcation),
    url(r'^dor/admin_handle/dormintory_handle/show_live_on_vacation_applyments',show_live_on_vacation_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_live_on_vacation_transcation',handle_live_on_vacation_transcation),
    url(r'^dor/admin_handle/repair_handle/show_repair_device_applyments',show_repair_device_applyments),
    url(r'^dor/admin_handle/repair_handle/handle_repair_device_applyment',handle_repair_device_applyment),
    url(r'^dor/admin_handle/device_handle/show_device_applyments',show_device_applyments),
    url(r'^dor/admin_handle/device_handle/commit_return_device',commit_return_device),
    url(r'^dor/admin_handle/device_handle/show_key_applyments',show_key_applyments),
    url(r'^dor/admin_handle/device_handle/show_minitor_applyments',show_minitor_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/show_meeting_room_applyments',show_meeting_room_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/handle_meeting_room_applyments',handle_meeting_room_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/show_meeting_room_info',show_meeting_room_info),
    url(r'^dor/admin_handle/activity_handle/show_activity_applyments',show_activity_applyments),
    url(r'^dor/admin_handle/activity_handle/handle_activity_applyments',handle_activity_applyments),
    url(r'^dor/admin_handle/activity_handle/show_activity_info',show_activity_info),
    url(r'^dor/admin_handle/activity_handle/new_activity',new_activity),
    url(r'^dor/admin_handle/book_handle/new_book',new_book),
    url(r'^dor/admin_handle/book_handle/show_books_info',show_books_info),
    url(r'^dor/admin_handle/search_handle/search_stu',search_stu),
    url(r'^dor/admin_handle/search_handle/sort_stu_info',sort_stu_info),
    url(r'^dor/admin_handle/search_handle/show_room_info',show_room_info),
    url(r'^dor/admin_handle/live_in_dor_handle/add_stu_dor_info',add_stu_dor_info),
    url(r'^dor/admin_handle/live_in_dor_handle/distribute_dor',distribute_dor),
    url(r'^dor/admin_handle/set_timequantum/set_timeable',set_timeable),
]