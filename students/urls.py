from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views
from students.views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = patterns('',
    url(r'^$', views.StudentListView.as_view(), name="list_view"),
    url(r'^(?P<pk>\d+)/', views.StudentDetailView.as_view(), name="detail"),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name="edit"),
    url(r'^add/', views.StudentCreateView.as_view(), name="add"),
    url(r'^remove/(?P<pk>\d+)/', views.StudentDeleteView.as_view(), name="remove"),
    url(r'^admin/', include(admin.site.urls)),
)
