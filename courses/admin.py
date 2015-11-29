from django.contrib import admin
from django.db import models
from django.forms import widgets
from courses.models import Course, Lesson
from django.contrib.admin.widgets import FilteredSelectMultiple

class LessonInline(admin.TabularInline):
	model = Lesson
	extra = 0

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'short_description']
	search_fields = ['name']
	inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)