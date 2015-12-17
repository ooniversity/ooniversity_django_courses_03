from django import forms
from students.models import Student

# Create your views here.
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
    
