# -*- coding:UTF-8 -*-

from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def list_view(request):
    courseId = request.GET.get('course_id', None)
    if courseId:
        students = Student.objects.filter(courses=Course.objects.get(id=courseId))
    else:
        students = Student.objects.all()
    cl = Course.objects.all()
    return render(request, 'students/list.html', {'students_list': students, 'courses_list': cl})


def detail(request, student_id):
    sd = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student_detail': sd})


def create(request):
    if request.POST:
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Студент " + form.cleaned_data['name'] + " " + form.cleaned_data[
                'surname'] + " успешно добавлен.".decode('utf-8')
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
            text = "Данные изменены.".decode('utf-8')
            messages.success(request, text)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    sd = Student.objects.get(id=student_id)
    if request.POST:
        text = "Студент " + str(sd) + " был удален.".decode('utf-8')
        messages.success(request, text)
        sd.delete()
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'sd': sd})
