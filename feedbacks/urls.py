from django.conf.urls import patterns, url
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
                       url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
                       )
