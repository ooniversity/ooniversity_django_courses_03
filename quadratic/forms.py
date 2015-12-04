# -*- coding: utf-8 -*-
from django import forms


class MyIntegerField(forms.IntegerField):
    default_error_messages = {
        'invalid': u'коэффициент не целое число',
    }


class QuadraticForm(forms.Form):
    a = MyIntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control input-sm', 'placeholder': 'Enter a:'}))
    b = MyIntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control input-sm', 'placeholder': 'Enter b:'}))
    c = MyIntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control input-sm', 'placeholder': 'Enter c:'}))

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError('коэффициент при первом слагаемом уравнения не может быть равным нулю')
        return self.cleaned_data['a']
