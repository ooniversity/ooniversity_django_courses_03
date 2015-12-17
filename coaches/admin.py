from django.contrib import admin
<<<<<<< HEAD
from coaches.models import Coach


# Register your models here.
class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description')
    list_filter = ['user__is_staff']


admin.site.register(Coach, CoachAdmin)
=======

<<<<<<< HEAD
from coaches.models import Coach 


class CoachAdmin(admin.ModelAdmin): 
    list_filter = ['description', 'gender', ] 
    list_display = ['description'] 

admin.site.register(Coach, CoachAdmin)

=======


>>>>>>> fb8e773dc2544433f2f086ca476591072179281d
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
