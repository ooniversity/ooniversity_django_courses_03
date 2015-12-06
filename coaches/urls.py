from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',url(r'(\d{1})/$', views.detail, name='detail'),)
