from django.contrib import admin

<<<<<<< HEAD
from coaches.models import Coach 


class CoachAdmin(admin.ModelAdmin): 
    list_filter = ['description', 'gender', ] 
    list_display = ['description'] 

admin.site.register(Coach, CoachAdmin)

=======


>>>>>>> fb8e773dc2544433f2f086ca476591072179281d
