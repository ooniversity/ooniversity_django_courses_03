from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render
from pybursa import views

from polls.views import polls_results


urlpatterns = patterns('',

=======
from pybursa import views


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
>>>>>>> bd2f98b40b2d5840ac070cb0260c3db1ea6b1992
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
<<<<<<< HEAD

    url(r'^polls/results/$', polls_results, name='polls_results'),

    url(r'^admin/', include(admin.site.urls)),
)
=======
    
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
)
>>>>>>> bd2f98b40b2d5840ac070cb0260c3db1ea6b1992
