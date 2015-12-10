from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from students.models import Student
from students.forms import StudentModelForm


# Create your views here.
class StudentListView(ListView):
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        students = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses=course_id)

        return students


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Student registration'
        return context

    def get_success_url(self):
        message = 'Account of {0} has been successfully added.'.format(self.object)
        messages.success(self.request, message)
        return reverse_lazy('students:list_view')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Student info update'
        return context

    def get_success_url(self):
        message = 'Info on the student has been successfully changed.'
        messages.success(self.request, message)
        return reverse_lazy('students:edit', kwargs={'pk': self.object.pk})


class StudentDeleteView(DeleteView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = 'Student info suppression'
        return context

    def get_success_url(self):
        message = 'Account  has been successfully removed.'
        messages.success(self.request, message)
        return reverse_lazy('students:list_view')
