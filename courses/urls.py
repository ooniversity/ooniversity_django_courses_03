from django.conf.urls import patterns, url
from courses.views import main, detail, add, edit, remove


urlpatterns = patterns('',
   url(r'^courses/(?P<pk>\d+)/$', detail, name='detail'),
   url(r'^$', main, name='list_view'),
   url(r'^courses/add/$', add, name='add'),
   url(r'^courses/edit/(?P<pk>\d+)/$', edit, name='edit'),
   url(r'^courses/remove/(?P<pk>\d+)/$', remove, name='remove'),
)
