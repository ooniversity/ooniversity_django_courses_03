from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from pybursa.views import index, contact
from feedbacks import views
admin.site.site_header = 'PyBursa Administration'

urlpatterns  =  patterns ( '' ,

    url(r'^$', index, name='index'),
    url(r'^courses/',  include('courses.urls', namespace = "courses")), 
    url(r'^polls/',  include('polls.urls',  namespace="polls")), 
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^contact/$', contact, name='contact'),
    url(r'^quadratic/', include('quadratic.urls')), 
    url(r'^students/', include('students.urls', namespace = "students")),
    url(r'^coaches/', include('coaches.urls', namespace = "coaches")),
    url(r'^feedback/', views.FeedbackView.as_view(), name='feedback'),
)
