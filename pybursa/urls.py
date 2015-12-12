from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render
from pybursa import views

from polls.views import polls_results


urlpatterns = patterns('',

=======
=======

>>>>>>> 7bad2329d865c7a6a913ed8f751121e0c20131e2
=======
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11
from pybursa import views


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
>>>>>>> bd2f98b40b2d5840ac070cb0260c3db1ea6b1992
    url(r'^$', views.index, name='index'),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
<<<<<<< HEAD
<<<<<<< HEAD

    url(r'^polls/results/$', polls_results, name='polls_results'),

    url(r'^admin/', include(admin.site.urls)),
)
=======
    
=======
>>>>>>> 7bad2329d865c7a6a913ed8f751121e0c20131e2
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)
>>>>>>> bd2f98b40b2d5840ac070cb0260c3db1ea6b1992
