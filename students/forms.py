from django.shortcuts import render
from django.views import generic
from students.models import Student
from django import forms
# Create your views here.


class StudentModelForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=100)
    skype = forms.CharField(max_length=50)
    #courses = forms.ManyToManyField(Course)


class DetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'

class ListView(generic.ListView):
    template_name = 'students/list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        return Student.objects.all()

def create(request):
    form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request):
    form = StudentModelForm()
    return render(request, 'students/edit.html', {'form': form})