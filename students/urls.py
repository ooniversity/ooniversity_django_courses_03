from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^(?P<student_id>\d+)/$', 'students.views.detail', name='detail'),
    url(r'^$', 'students.views.list_view', name='list_view'),
    url(r'^add/$', 'students.views.create', name='create'),
    url(r'^edit/(?P<student_id>\d+)/$', 'students.views.edit', name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$', 'students.views.remove', name='remove'),
    )