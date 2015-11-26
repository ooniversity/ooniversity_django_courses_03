from django.contrib import admin
from courses.models import Lesson, Course


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    inlines = [LessonInline]
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
