from django.conf.urls import patterns, url
from courses.views import main
from courses.views import detail


urlpatterns = patterns('',
   url(r'^courses/(?P<pk>\d+)/$', detail, name='detail'),
   url(r'^$', main, name='list_view'),
)
