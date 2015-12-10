# -*- coding: utf-8 -*- 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.forms import StudentModelForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from students.models import Student
from courses.models import Course



#ListView

class StudentListlView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students_on_course'

    def get_queryset(self):
        qs = super(StudentListlView, self).get_queryset()
        students_course = self.request.GET
        if 'course_id' in students_course:
            qs = qs.filter(courses=students_course['course_id'])
        return qs


#DetailView
class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'students_on_course'


#CreateView

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/add.html'
    form_class = StudentModelForm
    context_object_name = 'form'
    success_url = reverse_lazy('students:list_view')
    #success_message = u"Student %(name)s %(surname)s has been successfully added."
    
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context 

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, u"Student %s %s has been successfully added." % (student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)



#UpdeteView

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/edit.html'
    form_class = StudentModelForm
    context_object_name = 'form'
    success_message = u"Info on the student has been sucessfully changed."

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context 
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args = (self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(StudentUpdateView, self).form_valid(form)

        
#DeleteView

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/remove.html'
    success_url = reverse_lazy('students:list_view') 

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context 
    
    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        success_message = u"Info on {} {} has been sucessfully deleted.".format(self.object.name, self.object.surname)
        messages.success(self.request, success_message)
        return message


'''
def list_view(request):
    students_course = request.GET
    if 'course_id' in students_course:
        students_on_course = Student.objects.filter(courses=students_course['course_id'])
    else:  
        students_on_course = Student.objects.all()
    return render(request, 'students/list.html', {
			      "students_on_course": students_on_course ,
			       })


def detail(request, students_id):
	students_on_course = Student.objects.filter(pk=students_id)
	return render(request, 'students/detail.html', {
                  'students_on_course': students_on_course
                  })


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u"Student %s %s has been successfully added." % (application.name, application.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm() 
    return render(request, 'students/add.html', {
                  'form': form,
                  })


def edit(request, students_id):
    application = Student.objects.get(id=students_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, u"Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {
                  'form': form, 
                  })


def remove(request, students_id):
    application = Student.objects.get(id=students_id)
    remove_massage = u"Вы уверены, что хотите удалить студента %s %s ?" % (application.name, application.surname)
    if request.method == 'POST':
        application.delete()
        messages.success(request, u"Info on %s %s has been sucessfully deleted." % (application.name, application.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html',{
                  'remove_massage': remove_massage,
                  })
'''
