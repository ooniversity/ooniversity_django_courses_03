from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson

def detail(request, course_id):
    #return HttpResponse('course_id = {}'.format(course_id))
    args = {}
    
    course = Course.objects.get(id=course_id)
    args['name'] = course.name
    args['description'] = course.description
    args['lesson1'] = Lesson.objects.filter(course__id=course_id)
    args['crs_id'] = course_id
    #args['xuy'] = 'http://127.0.0.1:8000/students/?course_id={}'.format(course_id)





    return render(request, 'courses/detail.html', args)
