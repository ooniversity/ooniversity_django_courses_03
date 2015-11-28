from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['full_name' , 'email', 'skype']
    list_filter = ['courses']

    fieldsets = [('Personal Info', {'fields': ['name', 'surname', 'date_of_birth']}), ('Contact Info', {'fields': ['email', 'phone', 'address', 'skype', 'courses']})]
    raw_id_fields = ['courses']

    def full_name(self, obj):
     	return ("%s %s" % (obj.name, obj.surname))


admin.site.register(Student, StudentAdmin)