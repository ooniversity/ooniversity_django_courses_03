#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(label= u"коэффициент a")
    b = forms.FloatField(label= u"коэффициент b")
    c = forms.FloatField(label= u"коэффициент c")

