from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<r_id>\d+)/$', views.detail, name='detail'),
	url(r'^add/$', views.add , name = "add" ),
	url(r'^edit/(?P<c_id>[0-9]+)/$', views.edit, name = "edit"),
	url(r'^remove/(?P<c_id>[0-9]+)/$', views.remove, name = "remove"),
    url(r'^(?P<c_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)
