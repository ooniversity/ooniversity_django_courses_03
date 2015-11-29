from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views
from django.shortcuts import get_object_or_404, render


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index, name='index'),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^student_list/$', views.student_list, name='student_list' ),
    url(r'^student_detail/$', views.student_detail, name='student_detail' ),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)