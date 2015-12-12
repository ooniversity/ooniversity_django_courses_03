from django.conf.urls import patterns, url

from feedbacks import views

from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    
   url(r'^$', views.FeedbackView.as_view(), name="feedback"),
)
