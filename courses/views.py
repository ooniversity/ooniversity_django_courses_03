from django.shortcuts import render
import models


def index(request):
    items = models.Course.objects.all()
    return render(request, 'index.html', {'items': items})


def courses_info(request, num):
    item = models.Course.objects.get(id=num)
    lesson = models.Lesson.objects.filter(course=models.Course.objects.filter(id=num))
    return render(request, 'courses.html', {'item': item, 'lesson': lesson})


def contacts(request):
    return render(request, 'contact.html')


def student(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id)
    except:
        students = models.Student.objects.all()

    return render(request, 'students.html', {'students': students})


def student_detail(request, num):
    student = models.Student.objects.get(id = num)
    return render(request, 'student_detail.html', {'student': student})
