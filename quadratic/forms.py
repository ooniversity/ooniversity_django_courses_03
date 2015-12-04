from django import forms

class QuadraticForm(forms.Form):
  a = forms.IntegerField(label="coefficient a")
  b = forms.IntegerField(label="coefficient b")
  c = forms.IntegerField(label="coefficient c")
  
  def clean_a(self):
    a = self.cleaned_data['a']
    if a == 0:
      raise forms.ValidationError("Coefficient of first term of equation can not be zero")
    return self.cleaned_data['a']