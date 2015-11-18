from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import hello, contact, student, best

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', hello, name='index'),
	url(r'^contact/$', contact, name='contact'),
	url(r'^student_list/$', student, name='student_list'),
	url(r'^student_detail/$', best, name='student_detail'),
)
