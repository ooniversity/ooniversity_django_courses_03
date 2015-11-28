from django.conf.urls import include, url
from django.contrib import admin

from .views import contact, index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^$', index, name='index'),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^contact/$', contact, name='contact'),
]
