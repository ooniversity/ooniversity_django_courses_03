from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import *
from quadratic.views import *

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="index"),
    url(r'^contact/$', contact, name="contact"),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^quadratic/results/$', quadratic_results, name='results'),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)
