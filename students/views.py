<<<<<<< HEAD
<<<<<<< HEAD
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses = Course.objects.get(id = course_id))
        else:
            students = Student.objects.all()
        return students

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        messages.success(self.request, "Student " + form.cleaned_data['name'] + " " + form.cleaned_data['surname'] + " has been successfully added.")
        return super(StudentCreateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    
    def form_valid(self, form):
        messages.success(self.request, "Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, "Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context
=======
=======
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11
from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses = Course.objects.get(id = course_id))
        else:
            students = Student.objects.all()
        return students

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        messages.success(self.request, "Student " + form.cleaned_data['name'] + " " + form.cleaned_data['surname'] + " has been successfully added.")
        return super(StudentCreateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    
    def form_valid(self, form):
        messages.success(self.request, "Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, "Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

<<<<<<< HEAD
def list_view(request):
    q = request.GET.get('course_id', None)
    if q:
        sl = Student.objects.filter(courses = Course.objects.get(id = q))
    else:
        sl = Student.objects.all()
    cl = Course.objects.all()
    return render(request,'students/list.html', {'students_list' : sl, 'courses_list' : cl})

def detail(request, student_id):
    sd = Student.objects.get(id=student_id)
    return render(request,'students/detail.html', {'student_detail': sd} )

def create(request):
    if request.POST:
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Student " + form.cleaned_data['name'] + " " + form.cleaned_data['surname'] + " has been successfully added."
            messages.success(request, text)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, student_id):
    sd = Student.objects.get(id=student_id)
    form = StudentModelForm(instance=sd)
    if request.POST:
        form = StudentModelForm(request.POST, instance=sd)
        if form.is_valid():
            form.save()
            text = "Info on the student has been sucessfully changed."
            messages.success(request, text)
    return render(request, 'students/edit.html', {'form': form})    

def remove(request, student_id):
    sd = Student.objects.get(id=student_id)
    if request.method == "POST":
        text = "Info on " + str(sd) + " has been sucessfully deleted."
        messages.success(request, text)  
        sd.delete()
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'sd': sd})    
>>>>>>> 1ebe173911795743f7ef0495cc1b0aa19c8b3fa2
=======
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11
