from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
	url(r'^(?P<course_id>\d+)/$', views.detail, name="detail"),
	url(r'^add/$', views.add, name="add"),
	url(r'^edit/(?P<course_id>[0-9]+)/$', views.edit, name = "edit"),
	url(r'^remove/(?P<course_id>[0-9]+)/$', views.remove, name = "remove"),

	url(r'^add_lesson/$', views.add_lesson, name="add_lesson"),
)