from django.contrib import admin
import models

class LessonInline(admin.TabularInline):
    model = models.Lesson

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    search_fields = ['name']
    list_display = ('name', 'short_description')

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Lesson)