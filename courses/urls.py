from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'courses/(\d{1})/$', views.courses_info, name='courses'),
                       url(r'contact/$', views.contacts, name='contact'),
                       url(r'student_list/$', views.student_list, name='student_list'),
                       url(r'student_detail/$', views.student_detail, name='student_detail'),
                       )
