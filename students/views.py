from django.contrib import messages
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from courses.models import Course
from students.forms import StudentModelForm
from students.models import Student

# Create your views here.
class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super(StudentListView, self).get_context_data(**kwargs)
		#context['students'] = Student.objects.all()
		#context['paginator'] = Paginator(students, 2)
		#context['students'] = paginator.page(page)
		return context

	def get_queryset(self):
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			students = Student.objects.filter(courses__id = course_id)
		else:
			students = Student.objects.all()
		return students


class StudentDetailView(DetailView):
	model = Student


class StudentCreateView(CreateView):
	model = Student
	fields = '__all__'
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
		return context

	def form_valid(self, form):
		self.object = form.save()
		message = 'Student %s %s has been successfully added.' % (self.object.name, self.object.surname)
		messages.success(self.request, message)
		return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
	model = Student
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={'pk': self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Student info update"
		return context

	def form_valid(self, form):
		form.save()
		message = 'Info on the student has been sucessfully changed.'
		messages.success(self.request, message)
		return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
		return context

	def delete(self, request, *args, **kwargs):
		student = self.get_object()
		message = 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname)
		messages.success(self.request, message)
		return super(StudentDeleteView, self).delete(request, *args, **kwargs)


"""
def list_view(request):
	if request.GET.get('course_id'):
		course = Course.objects.get(id = request.GET.get('course_id'))
		students = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		students = Student.objects.all()
		course = Course.objects.all()
	return render(request, 'students/student_list.html', {'students':students})


def detail(request, student_id):
	student = Student.objects.get(id = student_id)
	return render(request, 'students/detail.html', {'student':student})


def create(request):
	if request.POST:
		form = StudentModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			messages.success(request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form':form})


def edit(request, student_id):
	student = Student.objects.get(id = student_id)
	if request.POST:
		form = StudentModelForm(request.POST, instance = student)
		if form.is_valid():
			student = form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
			return redirect('students:edit', student.id)
	else:
		form = StudentModelForm(instance = student)
	return render(request, 'students/edit.html', {'form':form})


def remove(request, student_id):
	student = Student.objects.get(id = student_id)
	if request.method == 'POST':
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
		student.delete()
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'student':student})
"""