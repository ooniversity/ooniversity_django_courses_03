from django.contrib import admin
import models

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    filter_horizontal = ['courses']
    search_fields = ('surname', 'email')
    list_display = ('full_name', 'email', 'skype')
    fieldsets = (('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']}))

admin.site.register(models.Student, StudentAdmin)