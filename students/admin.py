from django.contrib import admin
import models


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    
    filter_horizontal = ['courses']
    search_fields = ('surname', 'email')
    list_display = ('full_name', 'email', 'skype')
    


admin.site.register(models.Student, StudentAdmin)