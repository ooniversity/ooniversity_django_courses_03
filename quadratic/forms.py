#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(label= u"коэффициент a")
    b = forms.FloatField(label= u"коэффициент b")
    c = forms.FloatField(label= u"коэффициент c")

    def clean_a(self):
        data = self.cleaned_data['a']
        if int(data) == 0:
            raise forms.ValidationError(u'коэффициент при первом слагаемом уравнения не может быть равным нулю')

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data
