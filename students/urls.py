from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views


urlpatterns = [
    url(r'^$', views.students_list, name='student_list'),
]
