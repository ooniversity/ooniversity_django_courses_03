# -*- coding: utf-8 -*- 
from django import forms


class QuadraticForm(forms.Form):
	a = forms.FloatField(label='коэффициент a:')
	b = forms.FloatField(label='коэффициент b:')
	c = forms.FloatField(label='коэффициент c:')
'''	
	def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("You have forgotten about Fred!")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data
'''
