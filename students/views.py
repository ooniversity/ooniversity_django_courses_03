# -*- coding: utf-8 -*-
#from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
#from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    
    def get_queryset(self):
        if self.request.GET.get('course_id'):
            course = self.request.GET.get('course_id')
            students = Student.objects.filter(courses__id=course)
        else:
            students = Student.objects.all()
        return students    
    
    
    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        #students_list = Student.objects.all()
        paginator = Paginator(self.get_queryset(), 2) # Show 2 contacts per page

        page = self.request.GET.get('page')
        pages = []
        for number_page in paginator.page_range:
            pages.append(paginator.page(number_page))
        context['pages'] = pages
        context['course_id'] = self.request.GET.get('course_id')
        return context        




def list_view(request):

    args = {}

    if request.GET.get('course_id'):
        course = request.GET.get('course_id')
        st = Student.objects.filter(courses__id=course)
        args['students'] = st
    else:

        st = Student.objects.all()
        args['students'] = st

    return render(request, 'students/list.html', args)



class StudentDetailView(DetailView):
    model = Student
    #def get_context_data(self, **kwargs):
        #context = super(StudentDetailView, self).get_context_data(**kwargs)
        #context['courses'] = 

def detail(request, stud_id):

    args = {}
    args['stud_id'] = stud_id
    st = Student.objects.get(id=stud_id)
    args['student'] = st

    return render(request, 'students/detail.html', args)



class StudentCreateView(CreateView):
    model = Student
    #form_class = StudentModelForm
    #template_name = 'students/add.html'
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context
    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


def create(request):
    args = {}
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            surname = data['surname']            
            student = form.save()
            
            messages.success(request, 'Student %s %s has been successfully added.' % (name, surname))
            return redirect('students:list_view')
        else:
            form = StudentModelForm(request.POST)
            args['form'] = form
            return render(request, 'students/add.html', args)
    else:    
        form = StudentModelForm()
    
        args['form'] = form
        return render(request, 'students/add.html', args)

class StudentUpdateView(UpdateView):
    form_class = StudentModelForm
    model = Student
    #success_url = reverse_lazy('students:edit', get_object().id)
    def get_success_url(self):
        #if self.request.GET.get('pk'):
        #return reverse_lazy('students:edit', args=(self.request.GET.get('pk'), ))
        return reverse_lazy('students:edit', args=(self.get_object().id, ))
    
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context
    
    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)    



def edit(request, stud_id):
    args = {}
    student = Student.objects.get(id=stud_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            edit_student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            return redirect('students:edit', stud_id=stud_id)     
        else:
            args['form'] = form
            return render(request, 'students/edit.html', args)
    else:            

        form = StudentModelForm(instance=student)
        args['form'] = form
        return render(request, 'students/edit.html', args)


class StudentDeleteView(DeleteView):
    #form_class = StudentModelForm
    model = Student
    success_url = reverse_lazy('students:list_view')
    #success_message = "Thing %s was deleted successfully." 
     
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
    
    

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        surname = self.object.surname
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (name, surname))
        self.object.delete()
        return redirect(self.get_success_url())
    

def remove(request, stud_id):
    args = {}
    student = Student.objects.get(id=stud_id)
    if request.method == 'POST':
        
        
        name = student.name
        surname = student.surname
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (name, surname))
        return redirect('students:list_view')
    else:
        args['student'] = student
        return render (request, 'students/remove.html', args)




            