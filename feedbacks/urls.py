from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    url(r'^$', FeedbackView.as_view(), name = "feedback"),
)
