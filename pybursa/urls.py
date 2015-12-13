from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa.views import index, contact, student_list, student_detail
from quadratic.views import quadratic_results
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    #kz_3_1 and tutorial
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    #kz_3_2
    url(r'^$', index, name="index"),
    url(r'^contact/$', contact, name="contact"),
    #url(r'^student_list/$', student_list, name="student_list"),
    #url(r'^student_detail/$', student_detail, name="student_detail"),
    #kz_4
    url(r'^quadratic/', include('quadratic.urls', namespace='quadratic')),
    #kz_5
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    #kz_6
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    #kz_10
    url(r'^feedback/', FeedbackView.as_view(), name="feedback"),

)
