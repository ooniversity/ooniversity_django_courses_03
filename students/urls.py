from django.conf.urls import patterns, url
#from courses.models import Course
from students import views

urlpatterns = patterns('',
    #url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
	#url(r'^$', views.list_view, name='list_view'),
	#url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
	#url(r'^add/$', views.add, name='add'),
    #url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    #url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
	url(r'^$', views.StudentListView.as_view(), name='list_view'),
	url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
	url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
)
