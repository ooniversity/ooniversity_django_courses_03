# -*- coding: utf-8 -*
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from students.models import Student


class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        student = form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (
            student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    # template_name = 'students/add.html'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        messages.success(
            self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Student info suppression'
        return data

    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (
            self.object.name, self.object.surname))
        return message
