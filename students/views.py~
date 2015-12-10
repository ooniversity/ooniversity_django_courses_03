# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

class StudentListView(ListView):
	model = Student
	#context_object_name = 'students'
	def get_queryset(self):
		qs = super(StudentListView, self).get_queryset()
		course_id = self.request.GET.get('pk', None)
		if course_id:
			qs = qs.filter(courses = course_id)
		return qs	

"""
def list_view(request):
	if request.GET.get('course_id'):
		student = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		student = Student.objects.all()
	return render(request, 'students/list.html', {'students': student})
"""

class StudentDetailView(DetailView):
	model = Student
	def get_context_data(self, **kwargs):
		context = super(StudentDetailView,self).get_context_data(**kwargs)
		context['courses'] = Course.objects.filter(student__id = self.object.id)
		return context

"""
def detail(request, student_id):
	student = get_object_or_404(Student, id=student_id)
	return render(request, 'students/detail.html', {'student':student})
"""

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
		context['page_title'] = "Student registration"
		return context
	def form_valid(self, form):
		message = super(StudentCreateView, self).form_valid(form)
		mes = "Student %s %s has been successfully added." %(self.object.name, self.object.surname)
		messages.success(self.request, mes)
		return message

"""
def create(request):
	if request.method == "POST":
		form = StudentModelForm(request.POST)
		if form.is_valid():
			stud = form.save()
			mes = u'Студент %s %s успешно добавлен' %(stud.name, stud.surname)
			messages.success(request, mes)
			return redirect("students:list_view")
	else:
		form = StudentModelForm()
	return render(request, "students/add.html", {'form':form})
"""

class StudentUpdateView(UpdateView):
	model = Student
	def form_valid(self, form):
		message = super(StudentUpdateView, self).form_valid(form)
		mes = "Info on the student has been sucessfully changed."
		messages.success(self.request, mes)
		return message
	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={'pk':self.object.pk})
	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Student info update"
		context['page_title'] = "Student info update"
		return context


"""
def edit(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == "POST":
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			stud = form.save()
			mes = u'Данные изменены'
			messages.success(request, mes)
	else:
		form = StudentModelForm(instance=student)
	return render(request, "students/edit.html", {'form':form})
"""

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
		mes = "Info on %s %s has been sucessfully deleted." % (self.object.name, self.object.surname)
		messages.success(self.request, mes)
		return context
"""
def remove(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == "POST":
		student.delete()
		mes = u'Студент %s %s был удалён' %(student.name, student.surname)
		messages.success(request, mes)
		return redirect("students:list_view")

	return render(request, "students/remove.html", {'name':student.name, 'surname':student.surname})
"""	

