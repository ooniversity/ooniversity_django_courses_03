from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

class CoachAdmin (admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'skype', 'description')
    list_filter = ('user__is_staff', 'gender')
    
    def full_name(self, obj):
        return obj.user.get_full_name()  


admin.site.register(Coach, CoachAdmin)

