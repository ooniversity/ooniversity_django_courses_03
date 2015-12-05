from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages
from students.forms import StudentModelForm



def list_view(request):
    params = {}
    if request.GET.get('course_id'):
        params['students'] = Student.objects.filter(courses = request.GET.get('course_id'))
	params['course_id'] = request.GET.get('course_id')
    else:
        params['students'] = Student.objects.all()
    return render(request, 'students/list.html', params)

def create(request):
    params = {}
    if request.POST:
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            cleaned = form.cleaned_data
            messages.success(request, 'Student {0} {1} has been successfully added.'.format(cleaned['name'], cleaned['surname']))
        return redirect('students:list_view')
    else:
        form = StudentModelForm()
    params['form'] = form
    return render(request, 'students/add.html', params)

def edit(request, s_id):
    student = Student.objects.get(id = s_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = student)
        if form.is_valid():
            student = form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance = student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, s_id):
    params = {}
    student = Student.objects.get(id = s_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, u"Info on {0} {1} has been sucessfully deleted.".format(student.name, student.surname))
        return redirect('students:list_view')
    params['student'] = student
    return render(request, 'students/remove.html', params)

def detail (request, pk):
    params = {}
    params['student']=  Student.objects.get(id = pk)
    return render(request, 'students/detail.html', params)
