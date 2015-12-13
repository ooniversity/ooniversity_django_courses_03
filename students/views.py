# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm


'''
def list_view(request):
    try:
        qs= request.GET
        course = get_object_or_404(Course, pk=qs['course_id'])
        students = Student.objects.filter(courses__id = qs['course_id'])
        return render (request, 'students/list_view.html',{'course':course, 'students': students,})
    except:
        student_courses={}
        course = Course.objects.all()
        students = Student.objects.all()
        return render (request, 'students/list_view.html',{'course':course, 'students': students,})

def detail(request,student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = Course.objects.filter(student__id= student_id)
    return render (request, 'students/detail.html',{'courses':courses,'student': student})

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            stud = form.save()
            mes = u'Студент %s %s успешно добавлен.' %(stud.name, stud.surname)
            messages.success(request, mes)
            return redirect("students:list_view")
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {'form':form})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            stud = form.save()
            mes = u'Данные изменены.'
            messages.success(request, mes)
    else:
        form = StudentModelForm(instance=student)
    return render(request, "students/edit.html", {'form':form})

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        mes = u'Студент %s %s был удалён.' %(student.name, student.surname)
        messages.success(request, mes)
        return redirect("students:list_view")

    return render(request, "students/remove.html", {'name':student.name, 'surname':student.surname})
'''

class StudentListView(ListView):
    model = Student
    paginate_by = 2
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses = course_id)
        return qs


class StudentDetailView(DetailView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView,self).get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(student__id = self.object.id)
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context
    def form_valid(self, form):
        message = super(StudentCreateView, self).form_valid(form)
        mes = "Student %s %s has been successfully added." %(self.object.name, self.object.surname)
        messages.success(self.request, mes)
        return message


class StudentUpdateView(UpdateView):
    model = Student
    def form_valid(self, form):
        message = super(StudentUpdateView, self).form_valid(form)
        mes = "Info on the student has been sucessfully changed."
        messages.success(self.request, mes)
        return message
    def get_success_url(self):
        return reverse_lazy('students:edit', kwargs={'pk':self.object.pk})
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        mes = "Info on %s %s has been sucessfully deleted." % (self.object.name, self.object.surname)
        messages.success(self.request, mes)
        return context
