from django.shortcuts import render
from courses.models import Course, Lesson
# Create your views here.




def detail(request, id):
    course = Course.objects.get(id=id)
    lessons = course.lesson_set.all()
    return render(request, "courses/detail.html", {"course": course, "lessons": lessons})