from django.shortcuts import render, redirect
from courses.models import Course
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
    return render(request,
                  os.path.join('students', 'list.html'),
                  {'students': result})


def detail(request, request_id):
    result = {
      'student': Student.objects.get(id=request_id),
      'course': Course.objects.get(id=request_id)
      }
    return render(request, os.path.join('students', 'detail.html'), result)

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student_add = form.save()
            messages.success(
                request,
                'A user %s %s account created successfully' % (student_add.name, student_add.surname)
            )
            return redirect('students:list_view')
    else:
        form = StudentModelForm()

    data = {'form': form}

    return render(request,
                os.path.join('students', 'add.html'),
                data)


def edit(request, request_id):
    student = Student.objects.get(id=request_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=student)

    data = {'form': form}
    return render(request,
        os.path.join('students', 'edit.html'),
        data)


def remove(request, request_id):
    student = Student.objects.get(id=request_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request,
            'A user %s %s account is completely removed' % (student.name, student.surname))
        return redirect('students:list_view')

    message = 'Are you sure you want to delete account %s %s?' % (student.name, student.surname)

    data = {'err_message': message}
    return render(request,
            os.path.join('students', 'remove.html'),
            data)
