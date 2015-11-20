from django.conf.urls import patterns, include, url
from quadratic import views

urlpatterns = patterns('',
    url(r'^$', views.results, name='results'),
)
