from django.conf.urls import patterns, url
from django.contrib import admin
from feedbacks import views
from feedbacks.views import FeedbackView
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$', views.FeedbackView.as_view(), name='feedback'),
                       )
