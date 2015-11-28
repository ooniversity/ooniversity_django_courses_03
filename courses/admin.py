from django.contrib import admin
import models

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    search_fields = ['name']
    list_display = ('name', 'short_description')

class LessonInline(admin.TabularInline):
    extra = 0
    model = models.Lesson

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Lesson)    