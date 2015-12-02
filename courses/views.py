from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson
from django.core.exceptions import ObjectDoesNotExist

def detail(request, courses_id):
    try:
        courses = get_object_or_404(Course, pk=courses_id)
        lessons = courses.lesson_set.all()
        return render(request, 'courses/detail.html', { 
                      'courses':courses , 
                      'lessons':lessons,
                      })
    except ObjectDoesNotExist:
        achtung = "Houston, we have a problem with id = {0} exist yet.".format(courses_id) 
	return render(request, 'courses/detail.html', {
		    "achtung": achtung,
            })

            
