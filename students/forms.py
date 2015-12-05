from django.shortcuts import redirect, render
from django.views import generic
from students.models import Student
from django import forms
from django.contrib import messages
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


class DetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'

class ListView(generic.ListView):
    template_name = 'students/list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        return Student.objects.all()

def create(request):
    print request.POST
    #form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            student = Student()
            student.name = data['name']
            student.surname = data['surname']
            student.date_of_birth = data['date_of_birth']
            student.email = data['email']
            student.phone = data['phone']
            student.address = data['address']
            student.skype = data['skype']
            #student.courses = data['courses']
            student.save()
            messages.success(request, '%s %s was successfully added' % (student.name, student.surname))
            return redirect('students:list')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request):
    form = StudentModelForm()
    return render(request, 'students/edit.html', {'form': form})