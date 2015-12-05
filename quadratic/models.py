from django.db import models
from django import forms

class QuadraticForm(forms.Form):
    """Quadratic class"""
    a = forms.IntegerField(u"коэффициент a")
    b = forms.IntegerField(u"коэффициент b")
    c = forms.IntegerField(u"коэффициент c")

    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()
    def get_name(self):
        return self.user.first_name
    def get_surname(self):
        return self.user.last_name
    def get_is_stuff(self):
        return self.user.first_name
    def get_email(self):
        return self.user.email
    def __unicode__(self):
        return self.user.username
