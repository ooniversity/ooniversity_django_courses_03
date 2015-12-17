from django.conf.urls import patterns, url

<<<<<<< HEAD
from students import views

urlpatterns = patterns('',
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
=======
from . import views

urlpatterns = patterns('',
    #url(r'^(?P<pk>\d+)/$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='student_list'),
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
)
