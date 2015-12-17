from django.shortcuts import render,redirect
from students.models import Student
from students.forms import StudentModelForm
from courses.models import Course
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
import logging
logger = logging.getLogger(__name__)

class StudentDetailView(DetailView):
	model = Student	
	def get_context_data(self, **kwargs):
		logger.debug("Students detail view has been debugged")
		logger.info("Logger of students detail view informs you!")
		logger.warning("Logger of students detail view warns you!" )
		logger.error("Students detail view went wrong!")
		context = super(StudentDetailView, self).get_context_data(**kwargs)
		return context


class StudentListView(ListView):
	model = Student	
	paginate_by = 2
 
	def get_queryset(self):
		id_course= self.request.GET.get('course_id', None)
       # print id_course
		if id_course:
			students = Student.objects.filter(courses=id_course)
		else:
			students = Student.objects.all()
		return students


def list_view(request):
	try:
		id_course= request.GET['course_id']
		n_student = Student.objects.filter(courses=id_course)
	except:
		n_student = Student.objects.all()
	return render(request,'students/list.html',{'name_stud': n_student})


def detail(request, pk):
	n_student = Student.objects.filter(id=pk)
	return render(request,'students/student_detail.html',{'name_student': n_student[0]})


class StudentUpdateView(UpdateView):
	model = Student
	def get_success_url(self):
		return reverse('students:edit', kwargs={'pk': self.object.id})
	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Student info update"
		return context
	def form_valid(self, form):
		added_student = form.save()
		success_mes = 'Info on the student has been sucessfully changed.'
		messages.success(self.request, success_mes, extra_tags='msg')
  		return super(StudentUpdateView, self).form_valid(form)


def edit(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == 'POST': 
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			#print 
			student = form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.' )
			return redirect('students:edit', pk = student.id)
	else:
		form = StudentModelForm(instance=student)	
	return render(request,'students/edit.html', {'form' : form})	


class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
		return context
	def get_object(self):
		deleted_student = super(StudentDeleteView, self).get_object()
		messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (deleted_student.name, deleted_student.surname), extra_tags='msg')
		return deleted_student


def remove(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == 'POST':
		student.delete()
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
		return redirect('students:list_view')

	return render(request, 'students/remove.html', {'student': student})


class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	
	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
		return context
	def form_valid(self, form):
		added_student = form.save()
		success_mes = 'Student %s %s has been successfully added' % (added_student.name, added_student.surname)
		messages.success(self.request, success_mes, extra_tags='msg')
		return super(StudentCreateView, self).form_valid(form)



def create(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			student = form.save()
			messages.success(request, 'Student ' + data['name'] + " " + data['surname'] + ' has been successfully added.' )
			return redirect('students:list_view')
	else:
		form = StudentModelForm()		
	return render(request,'students/add.html', {'form' : form})	
