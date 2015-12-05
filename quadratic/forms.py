from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()