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
from templates import admin
from dor.views import show_admin_index,show_student_index,show_index
from dor.admin_handle.dormintory_handle import ad_handle_cancel_dor_transcation,ad_handle_change_dor_transcation,ad_handle_live_on_vacation_transcation,ad_show_cancel_dor_applyments,ad_show_change_dor_applyments,ad_show_live_on_vacation_applyments
from dor.admin_handle.repair_handle import  ad_show_repair_device_applyments,ad_handle_repair_device_applyment
from dor.admin_handle.device_handle import ad_show_device_applyments,ad_show_key_applyments,ad_show_minitor_applyments,ad_commit_return_device
from dor.admin_handle.meeting_room_handle import ad_show_meeting_room_applyments,ad_show_meeting_room_info,ad_handle_meeting_room_applyments
from dor.admin_handle.activity_handle import ad_show_activity_applyments,ad_show_activity_info,ad_handle_activity_applyments,ad_new_activity
from dor.admin_handle.book_handle import ad_new_book,ad_show_books_info
from dor.admin_handle.search_handle import ad_search_stu,ad_show_room_info,ad_sort_stu_info
from dor.admin_handle.live_in_dor_handle import ad_add_stu_dor_info,ad_distribute_dor
from dor.admin_handle.set_timequantum import ad_set_timeable
from dor.student_handle.dor_applyment import stu_change_dor_applyment, stu_cancel_dor_applyment, stu_live_on_vacation_applyment, stu_show_live_on_vacation_applyments, stu_show_cancel_dor_applyments, stu_show_change_dor_applyments
from dor.student_handle.resource_applyment import  stu_show_minitor_applyments, stu_show_key_applyments
from dor.student_handle.pay_bill import  stu_show_bill, stu_pay_bill
from dor.student_handle.activity_applyment import  stu_activity_applyment, stu_show_activity_info
from dor.student_handle.book_applyment import  stu_book_applyment, stu_my_borrowed_books, stu_my_shared_books, stu_show_book_info, stu_search_book
from dor.student_handle.meeting_room_applyment import  stu_meeting_room_applyment, stu_show_meeting_info
from dor.student_handle.device_repair_applyment import  stu_device_repair_applyment, stu_cancel_device_repair_applyment, stu_show_device_repair_applyments
urlpatterns = [
    url(r'^index/',show_index),
    url(r'^admin/',admin.site.urls),
    url(r'^show_admin_index',show_admin_index),
    url(r'^show_student_index',show_student_index),
    url(r'^dor/student_handle/dor_applyment/show_change_dor_applyments',stu_show_change_dor_applyments),
    url(r'^dor/student_handle/dor_applyment/change_dor_applyment',stu_change_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/show_cancel_dor_applyments',stu_show_cancel_dor_applyments),
    url(r'^dor/student_handle/dor_applyment/cancel_dor_applyment',stu_cancel_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/show_live_on_vacation_applyments',stu_show_live_on_vacation_applyments),
    url(r'^dor/student_handle/dor_applyment/live_on_vacation_applyment',stu_live_on_vacation_applyment),
    url(r'^dor/student_handle/device_repair_applyment/device_repair_applyment', stu_device_repair_applyment),
    url(r'^dor/student_handle/device_repair_applyment/show_device_repair_applyments',stu_show_device_repair_applyments),
    url(r'^dor/student_handle/device_repair_applyment/cancel_device_repair_applyment',stu_cancel_device_repair_applyment),
    url(r'^dor/student_handle/resource_applyment/show_minitor_applyments',stu_show_minitor_applyments),
    url(r'^dor/student_handle/resource_applyment/show_key_applyments',stu_show_key_applyments),
    url(r'^dor/student_handle/pay_bill/show_bill',stu_show_bill),
    url(r'^dor/student_handle/pay_bill/pay_bill',stu_pay_bill),
    url(r'^dor/student_handle/activity_applyment/activity_applyment',stu_activity_applyment),
    url(r'^dor/student_handle/activity_applyment/show_activity_info',stu_show_activity_info),
    url(r'^dor/student_handle/meeting_room_applyment/meeting_room_applyment',stu_meeting_room_applyment),
    url(r'^dor/student_handle/meeting_room_applyment/show_meeting_room_info', stu_show_meeting_info),
    url(r'^dor/student_handle/book_applyment/my_shared_books', stu_my_shared_books),
    url(r'^dor/student_handle/book_applyment/book_applyment',stu_book_applyment),
    url(r'^dor/student_handle/book_applyment/my_borrowed_books', stu_my_borrowed_books),
    url(r'^dor/student_handle/book_applyment/search_book',stu_search_book),
    url(r'^dor/student_handle/book_applyment/show_book_info',stu_show_book_info),


    url(r'^dor/admin_handle/dormintory_handle/show_change_dor_applyments', ad_show_change_dor_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_change_dor_transcation',ad_handle_change_dor_transcation),
    url(r'^dor/admin_handle/dormintory_handle/show_cancel_dor_applyments', ad_show_cancel_dor_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_cancel_dor_transcation',ad_handle_cancel_dor_transcation),
    url(r'^dor/admin_handle/dormintory_handle/show_live_on_vacation_applyments',ad_show_live_on_vacation_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_live_on_vacation_transcation',ad_handle_live_on_vacation_transcation),
    url(r'^dor/admin_handle/repair_handle/show_repair_device_applyments',ad_show_repair_device_applyments),
    url(r'^dor/admin_handle/repair_handle/handle_repair_device_applyment',ad_handle_repair_device_applyment),
    url(r'^dor/admin_handle/device_handle/show_device_applyments',ad_show_device_applyments),
    url(r'^dor/admin_handle/device_handle/commit_return_device',ad_commit_return_device),
    url(r'^dor/admin_handle/device_handle/show_key_applyments',ad_show_key_applyments),
    url(r'^dor/admin_handle/device_handle/show_minitor_applyments',ad_show_minitor_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/show_meeting_room_applyments',ad_show_meeting_room_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/handle_meeting_room_applyments',ad_handle_meeting_room_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/show_meeting_room_info',ad_show_meeting_room_info),
    url(r'^dor/admin_handle/activity_handle/show_activity_applyments',ad_show_activity_applyments),
    url(r'^dor/admin_handle/activity_handle/handle_activity_applyments',ad_handle_activity_applyments),
    url(r'^dor/admin_handle/activity_handle/show_activity_info',ad_show_activity_info),
    url(r'^dor/admin_handle/activity_handle/new_activity',ad_new_activity),
    url(r'^dor/admin_handle/book_handle/new_book',ad_new_book),
    url(r'^dor/admin_handle/book_handle/show_books_info',ad_show_books_info),
    url(r'^dor/admin_handle/search_handle/search_stu',ad_search_stu),
    url(r'^dor/admin_handle/search_handle/sort_stu_info',ad_sort_stu_info),
    url(r'^dor/admin_handle/search_handle/show_room_info',ad_show_room_info),
    url(r'^dor/admin_handle/live_in_dor_handle/add_stu_dor_info',ad_add_stu_dor_info),
    url(r'^dor/admin_handle/live_in_dor_handle/distribute_dor',ad_distribute_dor),
    url(r'^dor/admin_handle/set_timequantum/set_timeable',ad_set_timeable),
]