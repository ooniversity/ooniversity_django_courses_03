from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index, contact, student_list, student_detail
from quadratic.views import quadratic_results, calculate


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index, name='index'),
	url(r'^contact/$', contact, name='contact'),
	#url(r'^student_list/$', student_list, name='student_list'),
	url(r'^student_detail/', student_detail, name='student_detail'),
	#url(r'^quadratic/results/', quadratic_results, name='results'),
	url(r'^quadratic/results/$', calculate, name='calculate'),
	url(r'courses/', include('courses.urls', namespace="courses")),
	url(r'students/', include('students.urls', namespace="students")),
	url(r'coaches/', include('coaches.urls', namespace="coaches")),
)
