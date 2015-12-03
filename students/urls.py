from django.conf.urls import patterns, url

from students.views import list_view, detail, create, edit, remove

urlpatterns = patterns('',

                       url(r'^$', list_view, name='list_view'),
                       #url(r'^', list_view, name='list_view'),
                       url(r'^(?P<stud_id>\d+)/$', detail, name='detail'),
                       #url(r'^\d+', list_view, name='list_view'),
                       url(r'^add/$', create, name='add'),
                       url(r'^edit/(?P<stud_id>\d+)/$', edit, name='edit'),
                       url(r'^remove/(?P<stud_id>\d+)/$', remove, name='remove'),




                       )
