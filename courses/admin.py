from django.contrib import admin
import models


class LessonInline(admin.TabularInline):
    model = models.Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ['name']
    inlines = [LessonInline]

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Lesson)
