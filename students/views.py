from django.shortcuts import redirect, render
from django.views import generic
from students.models import Student
#from courses.models import Course
from students import forms
from django.contrib import messages
# Create your views here.


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'


class StudentListView(generic.ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students_list'

    #def get_queryset(self):
        #return Student.objects.all()
    #queryset = Student.objects.prefetch_related('courses')


def create(request):
    #print request.POST
    #form = StudentModelForm()
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            #data = form.cleaned_data
            #student = Student()
            #student.name = data['name']
            #student.surname = data['surname']
            #student.date_of_birth = data['date_of_birth']
            #student.email = data['email']
            #student.phone = data['phone']
            #student.address = data['address']
            #student.skype = data['skype']
            #student.courses = data['courses']
            #student.save()
            messages.success(request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
            return redirect('students:list')
    else:
        form = forms.StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = Student.objects.get(id=pk)
    #form = forms.StudentModelForm(instance=student)
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            return redirect('students:edit', pk)
    else:
        form = forms.StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return redirect('students:list')
    return render(request, 'students/remove.html', {'student': student})