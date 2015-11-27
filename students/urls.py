from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^(?P<student_id>\d+)/$', 'students.views.detail', name='detail'),
    url(r'^$', 'students.views.students', name='students'),
    )