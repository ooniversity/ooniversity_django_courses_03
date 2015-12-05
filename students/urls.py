from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views import list_view, detail, create, remove, edit


urlpatterns = patterns('',
    #url(r'^course_id=(?P<course_id>\d)/$', list_view, name='list_view'),
    url(r'^(?P<student_id>\d)/$', detail, name='detail'),
    url(r'^', list_view, name='list_view'),
    url(r'^add/$', create, name='add'),
    url(r'^remove/(?P<sid>\d+)/$', remove, name='remove'),
    url(r'^edit/(?P<sid>\d+)/$', edit, name='edit'),
)
