# -*- coding:UTF-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.CharField(label='коэффициент a', max_length=10)
    b = forms.CharField(label='коэффициент b', max_length=10)
    c = forms.CharField(label='коэффициент c', max_length=10)

    def clean_a(self):
        data = self.cleaned_data['a']
        if data.isalpha():
            raise forms.ValidationError("коэффициент не целое число")
        elif int(data) == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        elif data.isdigit():
            data = int(data)
        return data

    def clean_b(self):
        data = self.cleaned_data['b']
        if data.isalpha():
            raise forms.ValidationError("коэффициент не целое число")
        elif data.isdigit():
            data = int(data)
        return data

    def clean_c(self):
        data = self.cleaned_data['c']
        if data.isalpha():
            raise forms.ValidationError("коэффициент не целое число")
        elif data.isdigit():
            data = int(data)
        return data
