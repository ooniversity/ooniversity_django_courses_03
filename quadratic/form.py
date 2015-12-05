# -*- coding: utf-8 _*_
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(label="коэффициент а")
    b = forms.FloatField(label="коэффициент b")
    c = forms.FloatField(label="коэффициент c")

    def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнение не может быть равно нулю")
        return a
