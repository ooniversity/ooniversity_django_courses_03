from django.contrib import admin

from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'date_of_birth',  'email',  'phone',  'address',  'skype', 'courses']
    list_display = ('name', 'surname', 'email', 'skype')
    list_filter = ['courses']

admin.site.register(Student, StudentAdmin)
