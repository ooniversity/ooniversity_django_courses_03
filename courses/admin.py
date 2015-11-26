from django.contrib import admin
from courses.models import Course, Lesson


class LessonInLine(admin.TabularInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    inlines = [LessonInLine]
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
