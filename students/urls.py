from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^$', views.list_view, name='list_view'),
        url(r'^(\d{1})/$', views.detail, name='detail'),)
