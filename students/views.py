from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.edit import UpdateView

from students.forms import StudentModelForm

from polls.models import Choice, Question
from students.models import Student

class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses=course_id)
        return qs

"""
def list_view(request):
    try:
        course_id = request.GET['course_id']
        course_students = Student.objects.filter(courses = course_id)
    except:
        course_students = Student.objects.all()

    return render(request, 'students/list.html', {'course_students': course_students})
"""

class StudentDetailView(DetailView):
    model = Student

"""
def detail(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', {'student': student})
"""

"""
def create(request):

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            added_student = form.save()
            print added_student
            messages.success(request, 'Student %s %s has been successfully added' % (added_student.name, added_student.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {"form": form})
"""

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        added_student = form.save()
        success_mes = 'Student %s %s has been successfully added' % (added_student.name, added_student.surname)
        messages.success(self.request, success_mes, extra_tags='msg')
        return super(StudentCreateView, self).form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been sucessfully changed.', extra_tags='msg')
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('students:edit', kwargs={'pk': self.object.id})

"""
def edit(request, student_id):

    student = Student.objects.get(id=student_id)
    print student

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            print type(student.id)
            return redirect('students:edit', student_id = student.id)
    else:
        form = StudentModelForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})
"""

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def get_object(self):
        deleted_student = super(StudentDeleteView, self).get_object()
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (deleted_student.name, deleted_student.surname), extra_tags='msg')
        return deleted_student

"""
def remove(request, student_id):

    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return redirect('students:list_view')

    return render(request, 'students/remove.html', {'student': student})
"""

