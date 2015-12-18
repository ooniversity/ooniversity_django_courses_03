from django.contrib import admin
from courses.models import *


class LessonInline(admin.TabularInline):
    model = Lesson
    list_display = ['subject', 'description', 'order']
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    search_fields = ['name']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)

