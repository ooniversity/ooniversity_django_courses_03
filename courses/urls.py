from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views

urlpatterns = patterns('',
	#url(r'^$', list_view),
	url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name="detail"),
	url(r'^add/$', views.CourseCreateView.as_view(), name="add"),	
	url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name="edit"),
	url(r'remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name="remove"),
	url(r'^(?P<pk>\d+)/add_lesson$', views.LessonCreateView.as_view(), name='add-lesson'),
)

