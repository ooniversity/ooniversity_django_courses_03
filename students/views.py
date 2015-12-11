from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.models import Student
from students.forms import StudentModelForm


# Create your views here.
class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        students = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses__id=course_id)
        return students


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
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
        context['title'] = 'Student info update'
        return context

    def get_success_url(self):
        message = 'Info on the student has been successfully changed.'
        messages.success(self.request, message)
        return reverse_lazy('students:edit', kwargs={'pk': self.object.pk})


class StudentDeleteView(DeleteView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def get_success_url(self):
        student = self.get_object()
        message = 'Info on {} {} has been sucessfully deleted.'.format(student.name, student.surname)
        messages.success(self.request, message)
        return reverse_lazy('students:list_view')
