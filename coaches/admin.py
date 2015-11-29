from django.contrib import admin
from models import Coach
import models


class CoachAdmin(admin.ModelAdmin):
    #pass
    list_display=('get_first_name', 'get_last_name', 'gender', 'skype', 'description')
    list_filter = [('user__is_staff')]
    #print Coach.user__is_status
    

admin.site.register(Coach, CoachAdmin)
