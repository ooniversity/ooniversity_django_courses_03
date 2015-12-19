from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from students.models import Student
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
import logging

logger = logging.getLogger(__name__)


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        #logger.debug('Students detail view has been debugged')
        #logger.info('Logger of students detail view informs you!')
        #logger.warning('Logger of students detail view warns you!')
        #logger.error('Students detail view went wrong!!')
        return super(StudentDetailView, self).get_context_data(**kwargs)


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        else:
            students = Student.objects.all()
        return students

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        id = self.request.GET.get('course_id', None)
        if id:
            context['id_course'] = 'course_id=%s&' % id
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, u'Student %s %s has been successfully added.' % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        messages.success(self.request, u'Info on the student has been successfully changed.')
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
