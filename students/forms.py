from django import forms
from students.models import Student

# Create your views here.
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
    #name = forms.CharField(max_length=50)
    #surname = forms.CharField(max_length=50)
    #date_of_birth = forms.DateField()
    #email = forms.EmailField()
    #phone = forms.CharField(max_length=20)
    #address = forms.CharField(max_length=100)
    #skype = forms.CharField(max_length=50)
    #courses = forms.ManyToManyField(Course)