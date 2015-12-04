# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='a')
    b = forms.IntegerField(label='b')
    c = forms.IntegerField(label='c')

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError('not zero')
        return self.cleaned_data['a']