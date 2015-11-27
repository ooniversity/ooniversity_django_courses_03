from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views

urlpatterns = patterns('',
    url(r'^$', views.list_view, name="students"),
    url(r'^(?P<student_id>[1-9]+)/', views.detail, name="students"),
    url(r'^admin/', include(admin.site.urls)),
)
