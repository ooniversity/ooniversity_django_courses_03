from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    #sec = (self.name, self.surname)
    #full_name = ' '.join(sec)

admin.site.register(Student, StudentAdmin)
