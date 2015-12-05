from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
	url(r'^(?P<student_id>\d+)/$', views.detail, name="detail"),
	url(r'^$', views.list_view, name="list_view"),

	url(r'^add/', views.create, name="add"),
	url(r'^edit/(?P<student_id>[0-9]+)/$', views.edit, name="edit"),
	url(r'^remove/(?P<student_id>[0-9]+)/$', views.remove, name="remove")
)