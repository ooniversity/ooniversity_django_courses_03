from django.contrib import admin
from models import *

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']
    search_fields = ['name']

admin.site.register(Feedback, FeedbackAdmin)
