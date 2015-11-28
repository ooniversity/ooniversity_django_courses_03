from django.conf.urls import patterns, include, url
from django.contrib import admin

from courses import views

urlpatterns = patterns('',
      url(r'^(\d+)/$', views.detail, name = "detail"),
)