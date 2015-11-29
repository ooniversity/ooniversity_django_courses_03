from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index, contact, student_list, student_detail
from courses.views import *
from students.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    # url(r'^student_list/$', student_list, name='student_list'),
    # url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
)
