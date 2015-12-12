from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

admin.site.site_header = 'PyBursa Administration'

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls',namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^$', include('courses.urls')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
)



