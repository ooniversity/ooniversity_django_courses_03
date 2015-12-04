# -*- coding: utf-8 -*-
from django import forms
from __future__ import unicode_literals


class MyntegerField(forms.IntegerField):
    default_error_messages = {
        'invalid': 'Enter a whole number.',
    }

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control input-sm', 'placeholder': 'Enter a:'}))
    b = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control input-sm', 'placeholder': 'Enter b:'}))
    c = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control input-sm', 'placeholder': 'Enter c:'}))

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            # raise forms.ValidationError('If A=0, the equation is not quadratic.')
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return self.cleaned_data['a']
