# -*- coding: utf-8 -*- 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.forms import StudentModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from students.models import Student
from courses.models import Course
from django.views.generic.list import MultipleObjectMixin
import logging

logger = logging.getLogger(__name__)


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    #template_name = 'students/list.html'
    #context_object_name = 'students_on_course'

    def get_queryset(self):
        #students_on_course = super(StudentListView, self).get_queryset()
        students_course = self.request.GET
        if 'course_id' in students_course:
            #students = students_on_course.filter(courses=students_course['course_id'])
            students = Student.objects.filter(courses=students_course['course_id'])
        else:
            students = Student.objects.all()
        paginator = Paginator(students, 2) 
        return students


class StudentDetailView(DetailView):
    logger.debug("Students detail view has been debugged")
    logger.info("Logger of students detail view informs you!")
    logger.warning("Logger of students detail view warns you!")
    logger.error("Students detail view went wrong!")
    model = Student
    

class StudentCreateView(CreateView):
    model = Student
    #template_name = 'students/add.html'
    #form_class = StudentModelForm
    #context_object_name = 'form'
    success_url = reverse_lazy('students:list_view')
    #success_message = u"Student %(name)s %(surname)s has been successfully added."
    
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context 

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, u"Student %s %s has been successfully added." % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    #template_name = 'students/edit.html'
    #form_class = StudentModelForm
    #context_object_name = 'form'
    success_message = u"Info on the student has been sucessfully changed."

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context 
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args = (self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    #template_name = 'students/remove.html'
    success_url = reverse_lazy('students:list_view') 

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context 
    
    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        success_message = u"Info on {} {} has been sucessfully deleted.".format(self.object.name, self.object.surname)
        messages.success(self.request, success_message)
        return message



