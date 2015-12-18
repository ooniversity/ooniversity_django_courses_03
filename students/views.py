from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from students.models import Student
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
logger = logging.getLogger(__name__)

class StudentListView(ListView):

    model = Student
    paginate_by = 2

    def get_queryset(self):
        students = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course.id', None)
        if course_id:
            students = Student.objects.filter(courses = course_id)
        return students


class StudentDetailView(DetailView):

    model = Student
    logger.error("Students detail view went wrong!")
    logger.debug("Students detail view has been debugged")
    logger.info("Logger of students detail view informs you!")
    logger.warning("Logger of students detail view warns you!")


class StudentCreateView(CreateView):

    model = Student
    success_url = reverse_lazy('students:list_view')


    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        message = super(StudentCreateView, self).form_valid(form)
        mess = 'Student %s %s has been successfully added.' %(form['name'].value(), form['surname'].value())
        messages.success(self.request, mess)
        return message


class StudentUpdateView(UpdateView):

    model = Student
    success_url = reverse_lazy('students:list_view')


    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        message = super(StudentUpdateView, self).form_valid(form)
        mess = "Info on the student has been sucessfully changed."
        messages.success(self.request, mess)
        return message

class StudentDeleteView(DeleteView ):

    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context


    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        message_to_send = u'Info on {} {} has been sucessfully deleted.' .format(self.object.name, self.object.surname)
        messages.success(self.request, message_to_send)
        return message