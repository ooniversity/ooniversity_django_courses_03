from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views
from courses import views as courses_view

urlpatterns = patterns('',
    url(r'^$', courses_view.index, name='index'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Student
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),

    #Courses
     url(r'^courses/', include('courses.urls', namespace="courses")),

    #Students
     url(r'^students/', include('students.urls', namespace="students")),

    #Coaches
     url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)