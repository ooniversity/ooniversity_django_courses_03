from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course, Lesson
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
    if request.GET.get('course_id'):
        data_student = Student.objects.filter(courses = request.GET.get('course_id'))
    else:
        data_student = Student.objects.all()
    return render(request, 'students/list.html', {'students': data_student})

def detail(request, detail_id):
    return render(request, 'students/detail.html', {'student': Student.objects.get(id = detail_id)})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            message = u'Student {} {} has been successfully added.' .format(application.name, application.surname)
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
        application.delete()
        message = u'Info on {} {} has been sucessfully deleted.' .format(application.name, application.surname)
        messages.success(request, message)
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'name': application.name, 'surname': application.surname})

