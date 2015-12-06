from django.conf.urls import patterns, url
from courses.views import detail, add, edit, remove, add_lesson

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^add/$', add, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', remove, name='remove'),
    url(r'^(?P<pk>\d+)/add_lesson/$', add_lesson, name='add-lesson'),
    )
