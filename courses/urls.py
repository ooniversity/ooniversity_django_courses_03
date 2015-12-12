from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name = "detail"),
    url(r'^add/', views.CourseCreateView.as_view(), name="add"),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name="edit"),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name="remove"),
    url(r'^(?P<course_id>\d+)/add_lesson', views.add_lesson, name="add_lesson"),
=======
      # url(r'^$', pybursa.views.index, name="index")  
    url(r'^(?P<course_id>\d+)/$', views.detail, name = "detail"),
    url(r'^add/', views.add, name="add"),
    url(r'^edit/(?P<course_id>\d+)/$', views.edit, name="edit"),
    url(r'^remove/(?P<course_id>\d+)/$', views.remove, name="remove"),
    url(r'^(?P<course_id>\d+)add_lesson', views.add_lesson, name="add_lesson"),
>>>>>>> 1ebe173911795743f7ef0495cc1b0aa19c8b3fa2
)