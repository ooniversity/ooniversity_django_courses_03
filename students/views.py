# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from students.models import *
from students.forms import *
from django.contrib import messages

def list_view(request):
    r = request.GET
    if 'course_id' in r:
        students=Student.objects.filter(courses=r['course_id'])
    else:
        students=Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})

def create(request):
    context = {}
    if request.method == 'post':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, 'Student %s %s has been successfully added.' % (data['name'], data['surname']))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form' : form })

def edit(request, pk):
    form = StudentModelForm()
    student = Student.objects.get(id=pk)
    res={}   
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, 'Info on the student has been successfully changed.')            
    else:
        form = StudentModelForm(instance = student) 
    res['form'] = form
    return render(request, 'students/edit.html', res)

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (
            student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})