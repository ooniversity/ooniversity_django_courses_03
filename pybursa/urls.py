from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
import views
import students.views
from feedbacks.views import FeedbackView


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contact/',  views.contact, name='contact'),
    url(r'^feedback/', FeedbackView.as_view(), name='feedback'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
=======
from . import views

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('courses.urls')),#views.index, name='index',),
    url(r'^contact/', views.contact, name='contact',),
    url(r'^student_list/', include('students.urls', namespace='student_list')),
    url(r'^student_detail/', views.student_detail, name='student_detail',),
    url(r'^quadratic/results/$', include('quadratic.urls', namespace='quadratic',)),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    #url(r'^coaches/', include('coaches.urls', namespace='coaches')),
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
)
