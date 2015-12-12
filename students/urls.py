from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views

urlpatterns = patterns('',
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11
    url(r'^$', views.StudentListView.as_view(), name = "list_view"),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name = "detail"),
    url(r'^add/', views.StudentCreateView.as_view(), name="add"),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name="edit"),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name="remove"),
<<<<<<< HEAD
=======
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.list_view, name = "list_view"),
    url(r'^(?P<student_id>\d+)/$', views.detail, name = "detail"),
    url(r'^add/', views.create, name="add"),
    url(r'^edit/(?P<student_id>\d+)/$', views.edit, name="edit"),
    url(r'^remove/(?P<student_id>\d+)/$', views.remove, name="remove"),
>>>>>>> 1ebe173911795743f7ef0495cc1b0aa19c8b3fa2
=======
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11
)