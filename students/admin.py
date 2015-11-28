from django.contrib import admin
import models


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    


admin.site.register(models.Student, StudentAdmin)