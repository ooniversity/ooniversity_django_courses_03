from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from courses.models import Course, Lesson
from django.views import generic
from coaches.models import Coach




def courses(request, id_course):
	id_c = '?course_id=' + id_course
	n_lesson = Lesson.objects.filter(course_id=id_course)
	course = Course.objects.get(id=id_course)
	return render(request,'courses/detail.html',{'name_lesson': n_lesson,'course': course, 'id_c':id_c})


