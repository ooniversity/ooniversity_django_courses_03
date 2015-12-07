from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/', views.course, name='courses'),
    url(r'^admin/', include(admin.site.urls)),
)
