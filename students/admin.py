from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'skype']
    list_filter = ['courses']
    search_fields = ('surname', 'email',)

admin.site.register(Student,StudentAdmin)