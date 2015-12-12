from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views
# from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       # url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'contact/', views.contact, name='contact'),
                       # url(r'contact/', views.ContactView.as_view(), name='contact'),
                       # url(r'contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
                       url(r'students/', include('students.urls', namespace="students")),
                       url(r'courses/', include('courses.urls', namespace='courses')),
                       url(r'coaches/', include('coaches.urls', namespace="coaches")),
                       url(r'polls/', include('polls.urls', namespace="polls")),
                       url(r'^quadratic/', include('quadratic.urls')), )
