from django.shortcuts import render
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
    return render(request, 'students/add.html')

def edit(request):
    return render(request, 'students/edit.html')

def remove(request):
    return render(request, 'students/remove.html')










