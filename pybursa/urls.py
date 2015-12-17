from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import get_object_or_404, render
from feedbacks.views import FeedbackView
from pybursa import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^contact/', views.ContactView.as_view(), name='contact'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback")
)