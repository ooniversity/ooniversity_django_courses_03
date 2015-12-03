# -*- coding: utf-8 -*
from django import forms


class QuadraticForm(forms.Form):
    # create variables form
    a = forms.IntegerField(required=True)
    b = forms.IntegerField()
    c = forms.IntegerField()

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError(
                "коэффициент при первом слагаемом уравнения не может быть равным нулю")
            return data
