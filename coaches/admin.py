from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'desciption']

# Register your models here.
admin.site.register(Coach, CoachAdmin)

