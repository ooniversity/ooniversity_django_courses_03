from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
                       url(r'^([0-9]+)/$', views.detail, name='detail'),
                       url(r'^add/$', views.add, name='add'),
                       url(r'^edit/([0-9]+)/$', views.edit, name='edit'),
                       url(r'^remove/([0-9]+)/$', views.remove, name='remove'),
                       url(r'^([0-9]+)/add_lesson$', views.add_lesson, name='add_lesson'),
                       )
