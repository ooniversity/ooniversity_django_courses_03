"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import contact, index
from feedbacks.views import FeedbackView


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^contact/$', contact, name='contact'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^$', index, name='index'),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    )