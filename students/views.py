# -*- coding: utf-8 -*-
'''
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.models import Student


# Create your views here.

class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(
            self.request,
            'Student %s %s has been successfully added.' % (data['name'], data['surname']))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        messages.success(
            self.request, 'Info on the student has been sucessfully changed.')
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
        messages.success(
            self.request,
            'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)


'''
from students.models import Student
from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy


# Create your views here.


class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id and course_id.isdigit():
            return Student.objects.filter(courses=course_id)

        return Student.objects.all()


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        student = form.save()
        message = 'Student %s %s has been successfully added.' % (student.name, student.surname)
        messages.success(self.request, message)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student

    # form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def get_success_url(self, **kwargs):
        message = 'Info on the student has been sucessfully changed.'
        messages.success(self.request, message)
        return reverse_lazy('students:edit', args=(self.object.pk,))


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context


    def delete(self, request, **kwargs):
        student = self.get_object()
        message = super(StudentDeleteView, self).delete(request, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return message


