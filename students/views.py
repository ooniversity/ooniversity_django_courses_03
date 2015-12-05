from django.shortcuts import render, redirect

from courses.models import Course
from students.models import Student
from django.http import HttpResponse

def detail (request, pk):
    params = {}
    params['student']=  Student.objects.get(id = pk)
    return render(request, 'students/detail.html', params)

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
        params['form'] = StudentModelForm()
    return render(request, 'students/add.html', params)

def edit(request, s_id):
    params = {}
    student = Student.objects.get(id = student_id)
    if request.POST:
        form = StudentModelForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        params['form'] = StudentModelForm(instance = student)
    return render(request, 'students/edit.html', params )

def remove(request, s_id):
    params = {}
    params['student'] = Student.objects.get(id = student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', params)
