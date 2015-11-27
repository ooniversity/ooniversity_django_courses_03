from django.shortcuts import render
import models


def index(request):
    items = models.Course.objects.all()
    return render(request, 'index.html', {'items': items})


def courses_info(request, num):
    item = models.Course.objects.get(id=num)
    lesson = models.Lesson.objects.filter(course = models.Course.objects.filter(id=num))
    return render(request, 'courses.html', {'item': item, 'lesson': lesson})


def contacts(request):
    return render(request, 'contact.html')


def students(request):
    course_id = request.GET['course_id']
    students = models.Student.objects.filter()


    return render(request, 'students.html', {'course_id': course_id})


def student_detail(request):
    return render(request, 'student_detail.html')


