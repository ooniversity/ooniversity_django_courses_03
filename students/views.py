 # -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class StudentListView(ListView):
	model = Student

	def get_queryset(self):
		course_id = self.request.GET.get('course_id', None)
		if course_id:
			student = Student.objects.filter(courses = course_id)
		else:
			student = Student.objects.all()
		return student

class StudentDetailView(DetailView):
	model = Student

class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = "Student registration"
		context['button_name'] = "Создать"
		return context

	def form_valid(self, form):
		message = super(StudentCreateView, self).form_valid(form)
		success_message = "Student %s %s has been successfully added." %(self.object.name, self.object.surname)
		messages.success(self.request, success_message)
		return message

#def create(request):
#	if request.method == 'POST':
#		form = StudentModelForm(request.POST)
#		if form.is_valid():
#			student = form.save()
#			message_string = "Student %s has been successfully added." % student.fullname()
#			messages.success(request, message_string)
#		return redirect('students:list_view')
#	form = StudentModelForm()
#	return render(request, 'students/add.html', {'form': form})

class StudentUpdateView(UpdateView):
	model = Student
	def form_valid(self, form):
		message = super(StudentUpdateView, self).form_valid(form)
		success_message = "Info on the student has been sucessfully changed."
		messages.success(self.request, success_message)
		return message
	def get_success_url(self):
		return reverse_lazy('students:edit', kwargs={'pk':self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Student info update"
		context['button_name'] = "Сохранить"
		return context

#def edit(request, pk):
#   student = Student.objects.get(id=pk)
#  if request.method == 'POST':
#       form = StudentModelForm(request.POST, instance=student)
#       if form.is_valid():
#           student = form.save()
#           messages.success(request, "Info on the student has been sucessfully changed.")
#           return render(request, 'students/edit.html', {'form': form})
#
#   form = StudentModelForm(instance=student)
#   return render(request, 'students/edit.html', {'form': form})

class StudentDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy("students:list_view")

	def get_context_data(self, **kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Student info suppression"
		context['button_name'] = "Удалить"
		messages.success(self.request, "Info on %s has been sucessfully deleted." % self.object.fullname())
		return context

#def remove(request, pk):
#    student = Student.objects.get(id=pk)
#    if request.method == 'POST':
#        student.delete()
#        messages.success(request, "Info on %s has been sucessfully deleted." % student.fullname())
#        return redirect('students:list_view')
#
#    return render(request, 'students/remove.html', {'student': student})