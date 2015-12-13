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
