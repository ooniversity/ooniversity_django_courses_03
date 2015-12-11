from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']
    # list_filter = ['subject', 'create_date']


# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)
