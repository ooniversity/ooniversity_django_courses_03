from django.contrib import admin
import models


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    filter_horizontal = ['courses']


admin.site.register(models.Student, StudentAdmin)