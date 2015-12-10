from django.conf.urls import patterns, url

from students.views import list_view, detail, create, edit, remove, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = patterns('',

                       url(r'^$', StudentListView.as_view(), name='list_view'),
                       #url(r'^', list_view, name='list_view'),
                       url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='detail'),
                       #url(r'^\d+', list_view, name='list_view'),
                       url(r'^add/$', StudentCreateView.as_view(), name='add'),
                       url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='edit'),
                       url(r'^remove/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name='remove'),




                       )
