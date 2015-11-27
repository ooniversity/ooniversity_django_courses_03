from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'courses/(\d{1})/$', views.courses_info, name='courses'),
                       url(r'contact/$', views.contacts, name='contact'),
                       url(r'students/$', views.student, name='students'),
                       url(r'students/(\d{1})$', views.student_detail, name='student_detail'),
                       )
