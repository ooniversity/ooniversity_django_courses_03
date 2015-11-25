from django.conf.urls import patterns, url

from students.views import list_view, detail

urlpatterns = patterns('',

                       url(r'^$', list_view, name='list_view'),
                       #url(r'^', list_view, name='list_view'),
                       url(r'^(?P<stud_id>\d+)/$', detail, name='detail'),
                       #url(r'^\d+', list_view, name='list_view'),




                       )
