from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views
from feedbacks.views import FeedbackView


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
      #url(r'^student_list/$', student_list, name="student_list"),
      #url(r'^student_detail/$', student_detail, name="student_detail"),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^quadratic/results/$', include('quadratic.urls', namespace="quadratic")),
)
'''
handler404 = "pybursa.views.handler404"
handler500 = "pybursa.views.handler500"
'''
