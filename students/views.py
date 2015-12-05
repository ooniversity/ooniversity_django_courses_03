from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
import os


# Create your views here.
def list_view(request):
    replay = request.GET
    if 'course_id' in replay:
        result = Student.objects.filter(courses=replay['course_id'])
    else:
        result = Student.objects.all()
    return render(
        request,
        os.path.join('students', 'list.html'),
        {'students': result}
    )


def detail(request, pk):
    context = {'student': Student.objects.get(id=pk)}
    return render(
        request,
        os.path.join('students', 'detail.html'),
        context
    )


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student_add = form.save()
            messages.success(
                request,
                'Account of {0} {1} has been successfully added.'.format(student_add.name, student_add.surname)
            )
            return redirect('students:list_view')
    else:
        form = StudentModelForm()

    context = {'form': form}

    return render(
        request,
        os.path.join('students', 'add.html'),
        context
    )


def edit(request, pk):
    student_id = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=student_id)

    context = {'form': form}
    return render(
        request,
        os.path.join('students', 'edit.html'),
        context
    )


def remove(request, pk):
    student_id = Student.objects.get(id=pk)
    if request.method == 'POST':
        student_id.delete()
        messages.success(
            request,
            'Account  has been successfully removed.'.format(student_id.name, student_id.surname)
        )
        return redirect('students:list_view')

    context = {
        'notification': 'Are you sure you want to remove account of {0} {1}?'.format(
            student_id.name, student_id.surname)
    }
    return render(
        request,
        os.path.join('students', 'remove.html'),
        context
    )
