from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from students.models import Student
from courses.models import Course
from django.views import generic



def list_view(request):
	try:
		id_course= request.GET['course_id']
		n_student = Student.objects.filter(courses=id_course)
	except:
		n_student = Student.objects.all()
	return render(request,'students/list.html',{'name_stud': n_student})

def detail(request, id_student):
	n_student = Student.objects.filter(id=id_student)
	return render(request,'students/detail.html',{'name_student': n_student[0]})
	
