from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/',  views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls')),
)