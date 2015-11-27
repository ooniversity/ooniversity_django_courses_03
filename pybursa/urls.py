from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
import views

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    
    url(r'^$', views.index, name='index'), 
    url(r'^contact/', views.contact, name='contact'),
    #url(r'^courses/([0-9]+)/$', views.courses, name='courses'),
    #url(r'^courses/', views.courses, name='courses'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
