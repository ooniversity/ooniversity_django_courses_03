from django.contrib import admin
from django.db import models
from django.forms import widgets
from courses.models import Course, Lesson
from django.contrib.admin.widgets import FilteredSelectMultiple

class LessonInline(admin.StackedInline):
	model = Lesson
	fields = [ 'subject', 'description' , 'order' ]

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'short_description']
	search_fields = ['name']
	fields = [ 'name', 'short_description', 'description' ]
	inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
