# -*- coding: UTF-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()

    def clean_a(self):
        if self.cleaned_data['a'] == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return self.cleaned_data['a']
