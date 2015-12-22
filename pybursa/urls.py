from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin
from pybursa.views import index, contact, student_list, student_detail
from quadratic.views import quadratic_results
from django.views.generic import TemplateView
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^feedback/', FeedbackView.as_view(), name = "feedback"),
)