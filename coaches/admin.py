from django.contrib import admin

from coaches.models import Coach 


class CoachAdmin(admin.ModelAdmin): 
    list_filter = ['description', 'gender', ] 
    list_display = ['description'] 

admin.site.register(Coach, CoachAdmin)

