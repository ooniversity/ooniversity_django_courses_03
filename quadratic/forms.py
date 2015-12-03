# -*- coding: utf-8 -*-
from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(required=True, label = "коэффициент a")
    b = forms.IntegerField(required=True, label = "коэффициент b")
    c = forms.IntegerField(required=True, label = "коэффициент c")

    """
    def clean(self):
        cleaned_data = super(QuadraticForm, self).clean()
        a = cleaned_data.get("a")
        b = cleaned_data.get("b")
        c = cleaned_data.get("c")
        if not a:
            self.add_error('a', "коэффициент не определен")
        if not b:
            self.add_error('b', "коэффициент не определен")
    """
    def clean_a(self):
        a = self.cleaned_data['a']

        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")

        return a
