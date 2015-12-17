from django.contrib import admin
<<<<<<< HEAD
from students.models import Student


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
    search_fields = ['surname', 'email']
    list_filter = ['courses']
    filter_horizontal = ('courses',)
    fieldsets = (
        ('Personal info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),
       ('Contact info', {
            'fields': ('email', 'phone', 'address', 'skype')
        }),
        (None, {
            'fields': ('courses',)
        }),
    )
    
admin.site.register(Student, StudentAdmin)


=======

from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'date_of_birth',  'email',  'phone',  'address',  'skype', 'courses']
    list_display = ('name', 'surname', 'email', 'skype')
    list_filter = ['courses']

admin.site.register(Student, StudentAdmin)
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
