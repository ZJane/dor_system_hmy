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
from dor.views import show_index,show_student_index
from dor.admin_handle.dormintory_handle import handle_cancel_dor_transcation,handle_change_dor_transcation
from dor.student_handle.dor_applyment import change_dor_applyment,cancel_dor_applyment,live_on_vacation_applyment
urlpatterns = [
    url(r'^show_index',show_index),
    url(r'^show_student_index',show_student_index),
    url(r'^dor/student_handle/dor_applyment/change_dor_applyment',change_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/cancel_dor_applyment',cancel_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/live_on_vacation_applyment',live_on_vacation_applyment),
    url(r'^dor/admin_handle/dormintory_handle/handle_change_dor_transcation',handle_change_dor_transcation),
    url(r'^dor/admin_handle/dormintory_handle/handle_cancel_dor_transcation',handle_cancel_dor_transcation)
]