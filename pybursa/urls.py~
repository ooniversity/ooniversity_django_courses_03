from django.conf.urls import patterns, include, url
from django.contrib import admin
#from .views import index, student_list, student_detail, contact
#from .views import *
import views
import students.views
from feedbacks.views import FeedbackView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    #http://127.0.0.1:8000/polls/latest.html
    #url(r'^polls/latest\.html$', 'polls.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contact/',  views.contact, name='contact'),
    url(r'^feedback/', FeedbackView.as_view(), name='feedback'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)
