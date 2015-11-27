from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'contact/$', views.contact, name='contact'),
                       url(r'^courses/',include('courses.urls', namespace='courses')),
                       url(r'^students/',include('students.urls', namespace='students')),
                       )
