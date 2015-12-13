from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views


urlpatterns = [
    url(r'^$', views.StudentListlView.as_view(), name='student_list'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='student_add'),
    url(r'^edit/(?P<pk>\d+)$',  views.StudentUpdateView.as_view(), name='student_edit'),
    url(r'^del/(?P<pk>\d+)$', views.StudentDeleteView.as_view(), name='student_del'),
    url(r'detail/(?P<pk>\d+)$', views.StudentDetailView.as_view(), name='student_detail')

]
