from django.contrib import admin
from .models import Coach

#class CoursesAdmin(admin.ModelAdmin):
#    list_display = ['name','short_description']
#    search_fields = ['name']

admin.site.register(Coach)
