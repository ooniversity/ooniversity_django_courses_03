from django.shortcuts import render, redirect
from django.contrib import messages
from students.forms import StudentModelForm
import models


def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
    except:
        students = models.Student.objects.all()

    return render(request, 'students/list.html', {'students': students})


def detail(request, pk):
    student = models.Student.objects.get(id=pk)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            message_string = "Student %s has been successfully added." % student.fullname()
            messages.success(request, message_string)
            return redirect('students:list_view')

    form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = models.Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
            return render(request, 'students/edit.html', {'form': form})

    form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = models.Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Info on %s has been sucessfully deleted." % student.fullname())
        return redirect('students:list_view')

    return render(request, 'students/remove.html', {'student': student})





