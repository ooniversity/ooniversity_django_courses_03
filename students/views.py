# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView   
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
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
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Student %s %s has been successfully added.' % (data['name'], data['surname']))
        return super(StudentCreateView, self).form_valid(form)

class StudentListView(ListView):
      model = Student
      
      def get_queryset(self):
          qs = super(StudentListView, self).get_queryset()
          course_id = self.request.GET.get('course_id', None)
          if course_id:
              qs = qs.filter(courses__id=course_id)
          return qs


class StudentDetailView(DetailView):
    model = Student


def list_view(request):
  course_id = request.GET.get('course_id')
  if course_id != None and course_id != '':
    course = Course.objects.get(id=course_id)
    stud = Student.objects.all()
    students = []
    for man in stud:
      if course in man.courses.all():
        students.append(man)
    return render(request, 'students/list.html', {'students':students})
  else:
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students':students})

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student':student})

def create(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            add_stud = form.save()
            messages.success(request, u'Student %s %s has been successfully added.' % (add_stud.name, add_stud.surname))
            return redirect('students:list_view')
    return render(request,'students/add.html',{'form':form})

def remove(request,pk):
    student = Student.objects.get(id=pk)
    message = u"%s %s" %(student.name, student.surname)
    if request.method == 'POST':
        student.delete()
        messages.success(request, u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'message': message})

def edit(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)
    return render(request,'students/edit.html',{'form':form})