from django.conf.urls import patterns, url

from . import views

#urlpatterns = patterns('',
    #url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
#)

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/courses/$', views.LessonsView.as_view(), name='lessons'),
)
  
#url(r'^detail/$', CourseListView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view()),
