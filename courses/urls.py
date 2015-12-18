from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name="detail"),
	url(r'^add/$', views.CourseCreateView.as_view(), name="add"),
	url(r'^edit/(?P<pk>[0-9]+)/$', views.CourseUpdateView.as_view(), name = "edit"),
	url(r'^remove/(?P<pk>[0-9]+)/$', views.CourseDeleteView.as_view(), name = "remove"),

	url(r'^(?P<pk>[0-9]+)/add_lesson$', views.LessonCreateView.as_view(), name="add-lesson"),
)