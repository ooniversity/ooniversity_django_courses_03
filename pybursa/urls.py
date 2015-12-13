from django.conf.urls import patterns, include, url
from django.contrib import admin
from feedbacks.views import FeedbackView
import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^courses/', include('courses.urls', namespace='courses')),
                       url(r'^students/', include('students.urls', namespace='students')),
                       url(r'^coaches/', include('coaches.urls', namespace='coaches')),
                       url(r'^quadratic/', include('quadratic.urls', namespace='quadratic')),
                       )
