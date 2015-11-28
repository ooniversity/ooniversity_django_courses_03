from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ['get_name', 'email', 'skype']
    list_filter = ['courses']
    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None, {'fields': ['courses']})
    ]
    filter_horizontal = ['courses']

    def get_name(self, instance):
        return '{0} {1}'.format(instance.name, instance.surname)

    get_name.short_description = 'Full name'
    get_name.admin_order_field = 'Name'


# Register your models here.
admin.site.register(Student, StudentAdmin)
