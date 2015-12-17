from django.conf.urls import patterns, url

<<<<<<< HEAD
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<pk>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)
=======
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
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
