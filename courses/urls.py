from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', 'courses.views.detail', name='detail'),
    #url(r'^(?P<course_id>\d+)/$', 'courses.views.detail', name='detail'),
    )