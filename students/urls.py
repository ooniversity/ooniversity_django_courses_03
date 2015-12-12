from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views


urlpatterns = [
    url(r'^$', views.students_list, name='student_list'),
    url(r'^add/$', views.add_student, name='student_list'),
    url(r'detail/(?P<pk>\d+)$', views.StudentDetailView.as_view(), name='student_detail')

]
