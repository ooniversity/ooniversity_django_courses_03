# -*- coding: utf-8 -*-
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import logging


logger = logging.getLogger(__name__) #students.view


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    
    def get_queryset(self):
    	r = self.request.GET
    	if 'course_id' in r:
    		students = Student.objects.filter(courses=r['course_id'])
    	else:
    		students = Student.objects.all()
    	return students
    
	        
class StudentDetailView(DetailView):
	logger.debug("Students detail view has been debugged")
	logger.info("Logger of students detail view informs you!")
	logger.warning("Logger of students detail view warns you!")
	logger.error("Students detail view went wrong!")
	model = Student
    

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view') 
    
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context
    
    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    
    def get_success_url(self):
        return reverse('students:edit', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context
        
    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)
        
      
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
        
    def delete(self, request, pk, *args, **kwargs):
        application = Student.objects.get(id=pk)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)


        
''' 
def list_view(request):
	r = request.GET
	if 'course_id' in r:
		students = Student.objects.filter(courses=r['course_id'])
	else:
		students = Student.objects.all()
	return render(request, 'students/list.html', {'students': students})
  
  
def detail(request, pk):
	students = Student.objects.filter(id=pk)
	return render(request, 'students/detail.html', {'students': students})
  
  
def create(request):
	if request.method == 'POST':	
		model_form = StudentModelForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			name = model_form.cleaned_data['name']
			surname = model_form.cleaned_data['surname']
			messages.success(request, 'Student %s %s has been successfully added.' % (name, surname))
			return redirect('students:list_view')
	else:
		model_form = StudentModelForm()
	return render(request, 'students/add.html', {'model_form': model_form})


def edit(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':	
		model_form = StudentModelForm(request.POST, instance=application)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
			return redirect('students:edit', application.id)
	else:
		model_form = StudentModelForm(instance=application)
	return render(request, 'students/edit.html', {'model_form': model_form})
	

def remove(request, pk):
	application = Student.objects.get(id=pk)
	if request.method == 'POST':
		application.delete()	
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname))
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'application': application})	
'''	
