from django.conf.urls import patterns, include, url
from feedbacks import views

urlpatterns = patterns('',
	url(r'^$', views.StudentListView.as_view(), name="feedback"),
)