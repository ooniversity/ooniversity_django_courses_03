from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Student
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),

    #Courses
     url(r'^', include('courses.urls', namespace="courses")),

    #Students
     url(r'^students/', include('students.urls', namespace="students")),
)