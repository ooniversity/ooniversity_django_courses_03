# -*- coding:UTF-8 -*-
from django.shortcuts import render,  get_object_or_404, redirect
from django.db import models
import models
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from students.models import Student



def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
        selection = True
    except:
        students = models.Student.objects.all()
        selection = False

    return render(request, 'students/list_view.html', {'students': students,
        'selection': selection})


def detail(request, student_id):
    student = models.Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.POST:
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Студент " + form.cleaned_data['name'] + " " + form.cleaned_data['surname'] + " успешно добавлен"
            messages.success(request, text)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    sd = Student.objects.get(id=student_id)
    form = StudentModelForm(instance=sd)
    if request.POST:
        form = StudentModelForm(request.POST, instance=sd)
        if form.is_valid():
            form.save()
            text = "Информация о студенте успешно изменена"
            messages.success(request, text)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    sd = Student.objects.get(id=student_id)
    if request.POST:
        text = "Информация о " + str(sd) + " была успешно удалена"
        messages.success(request, text)
        sd.delete()
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'sd': sd})
