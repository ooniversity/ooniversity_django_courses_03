# -*- coding: UTF-8 -*-
from django import forms


class QuadraticForm(forms.Form):

    a = forms.FloatField(label="коэффициент c")
    b = forms.FloatField(label="коэффициент b")
    c = forms.FloatField(label="коэффициент c")

    def clean_a(self):
        if self.cleaned_data['a'] == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return self.cleaned_data['a']
