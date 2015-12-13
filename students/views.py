from django.shortcuts import render, redirect
from django.contrib import messages
from students.forms import StudentModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import MultipleObjectMixin
import models


def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
    except:
        students = models.Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})


def detail(request, pk):
    student = models.Student.objects.get(id=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            message_string = "Student %s has been successfully added." % student.fullname()
            messages.success(request, message_string)
            return redirect('students:list_view')

    form = StudentModelForm()
    return render(request, 'students/student_form.html', {'form': form})


def edit(request, pk):
    student = models.Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
            return render(request, 'students/edit.html', {'form': form})

    form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = models.Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Info on %s has been sucessfully deleted." % student.fullname())
        return redirect('students:list_view')

    return render(request, 'students/student_confirm_delete.html', {'student': student})


class StudentListView(ListView, MultipleObjectMixin):
    model = models.Student
    paginate_by = 2

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id).order_by('id')
        return qs


class StudentDetailView(DetailView):
    model = models.Student


class StudentCreateView(CreateView):
    model = models.Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Student registration"
        return context

    def form_valid(self, form):
        student = form.save()
        message_string = "Student %s has been successfully added." % student.fullname()
        messages.success(self.request, message_string)
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = models.Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context

    def form_valid(self, form):
        student = form.save()
        message_string = "Info on the student has been sucessfully changed."
        messages.success(self.request, message_string)
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        student = kwargs['object']
        messages.success(self.request, "Info on %s has been sucessfully deleted." % student.fullname())
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        return context
