from django.conf.urls import patterns, url

from courses import views



urlpatterns = patterns('',
    
    url(r'^([0-9]+)/$', views.courses, name='detail'),
    url(r'^edit/(?P<course_id>\d+)/', views.edit, name="edit"),
    url(r'^add/$', views.add, name="add"),
    url(r'^remove/(?P<course_id>\d+)/', views.remove, name="remove"),
    url(r'^(?P<course_id>[1-9]+)/add_lesson', views.add_lesson, name="add-lesson"),

)
