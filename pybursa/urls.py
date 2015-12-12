from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

from feedbacks.views import FeedbackView

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^feedback/', FeedbackView.as_view(), name="feedback"),

    url(r'^$', views.IndexTemplateView.as_view(), name="index"),
    url(r'^contact', TemplateView.as_view(template_name="contact.html"), name="contact"),

    url(r'^courses/',include('courses.urls', namespace="courses")),
    url(r'^students/',include('students.urls', namespace="students")),
    url(r'^coaches/',include('coaches.urls', namespace="coaches")),
)