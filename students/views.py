from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from students.forms import StudentModelForm
from students.models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

"""
def list_view(request):
	try:
		id_course= request.GET['course_id']
		n_student = Student.objects.filter(courses=id_course)
	except:
		n_student = Student.objects.all()
	return render(request,'students/list.html',{'name_stud': n_student})
"""	

class StudentListView(ListView):
	model = Student
	#template_name = 'students/list.html'
	#context_object_name = 'name_stud'
	def get_queryset(self):
		qs = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(courses=course_id)
		return qs




class StudentDetailView(DetailView):
	model = Student
	#template_name = 'students/detail.html'
	#context_object_name = 'name_student'
"""		
def detail(request, id_student):
	n_student = Student.objects.filter(id=id_student)
	return render(request,'students/detail.html',{'name_student': n_student[0]})
"""	
class StudentCreateView(CreateView):
	model = Student
	#template_name = 'students/add.html'
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

"""		
def create(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			added_student = form.save()
			messages.success(request, 'Student %s %s has been successfully added' % (added_student.name, added_student.surname))
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {"form": form}
"""	
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
"""
def edit(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
			return redirect('students:edit', student_id = student.id)
	else:
		form = StudentModelForm(instance=student)
	return render(request, 'students/edit.html', {'form': form})
"""
class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	#def get_success_url(self):
		#return reverse('students:edit', kwargs={'pk': self.object.id})
	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
 		return context
	def get_object(self):
		deleted_student = super(StudentDeleteView, self).get_object()
		messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (deleted_student.name, deleted_student.surname), extra_tags='msg')
		return deleted_student
"""
def remove(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == 'POST':
		student.delete()
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'student': student})
"""	

