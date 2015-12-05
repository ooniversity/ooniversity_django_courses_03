from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

from students.forms import StudentModelForm
from students.models import Student

def list_view(request):
    reguest_course = request.GET
    if 'course_id' in reguest_course:
        list_students = Student.objects.filter(
            courses=reguest_course['course_id'])
    else:
        list_students = Student.objects.all()
    return render(request, 'students/list.html', {'list_students': list_students})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    context = {}
    if request.method == "POST":
        context['form'] = form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            data = form.cleaned_data
            messages.success(request, 'Student %s %s has been successfully added.' % (
                student.name, student.surname))
            return redirect('students:list_view')

    else:
        context['form'] = StudentModelForm()
    return render(request, 'students/add.html', context)


def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(
                request, 'Info on the student has been sucessfully changed.')
            # return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (
            student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})

