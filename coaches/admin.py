from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display =  ['get_first_name', 'get_last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']

    def get_first_name(self, obj):
    	return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
    	return obj.user.last_name
    get_last_name.short_description = 'Last Name'
    
admin.site.register(Coach, CoachAdmin)

