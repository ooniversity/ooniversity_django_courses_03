from django.shortcuts import render
from students.models import Student

def list_view(request):
	try:
		id_course= request.GET['course_id']
		print request.GET['course_id']
		n_student = Student.objects.filter(courses=id_course)
	except:
		n_student = Student.objects.all()
		print 'hfhdjkhjkgh'
	return render(request,'students/list.html',{'name_stud': n_student})

def detail(request, id_student):
	n_student = Student.objects.filter(id=id_student)
	return render(request,'students/detail.html',{'name_student': n_student[0]})
