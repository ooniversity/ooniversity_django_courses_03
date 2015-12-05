from students.forms import StudentModelForm
from django.shortcuts import render, redirect
import models


def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
    except:
        students = models.Student.objects.all()

    return render(request, 'students/list.html', {'students': students})


def detail(request, num):
    student = models.Student.objects.get(id = num)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    context = {}
    if request.method == 'POST': 
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    context = {'form': form}
    return render(request, 'students/add.html', context)


def edit(request):
    return render(request, 'students/edit.html')

def remove(request):
    return render(request, 'students/remove.html')










