from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from students.forms import StudentModelForm

from polls.models import Choice, Question
from students.models import Student

def list_view(request):
    try:
        course_id = request.GET['course_id']
        course_students = Student.objects.filter(courses = course_id)
    except:
        course_students = Student.objects.all()

    return render(request, 'students/list.html', {'course_students': course_students})

def detail(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', {'student': student})

def create(request):

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            added_student = form.save()
            print added_student
            messages.success(request, 'Student %s %s has been successfully added' % (added_student.name, added_student.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()


    return render(request, 'students/add.html', {"form": form})

def edit(request, student_id):

    student = Student.objects.get(id=student_id)
    print student

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            print type(student.id)
            return redirect('students:edit', student_id = student.id)
    else:
        form = StudentModelForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):

    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return redirect('students:list_view')

    return render(request, 'students/remove.html', {'student': student})

