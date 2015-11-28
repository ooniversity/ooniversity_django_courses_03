from django.contrib import admin
from students.models import Student
from courses.models import Course, Lesson
class StudentAdmin(admin.ModelAdmin):
    list_filter = ['courses']
    list_display = ['full_name', 'email', 'skype']
    filter_horizontal = ('courses',)
    fieldsets = [('Personal info',{'fields':['name','surname','date_of_birth']}),('Contact info',{'fields':['email','phone','address','skype']}),(None,{'fields':['courses']})]
    search_fields = ['surname', 'email']
admin.site.register(Student, StudentAdmin)
