from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic.views import quadratic_results
from pybursa.views import index, contact, student_list, student_detail


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index, name='index'),
	url(r'^contact/$', contact, name='contact'),
	url(r'quadratic/', include('quadratic.urls')),
	url(r'courses/', include('courses.urls', namespace="courses")),
	url(r'students/', include('students.urls', namespace="students")),
	url(r'coaches/', include('coaches.urls', namespace="coaches")),
)
