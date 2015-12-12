from django.contrib import messages
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView



def students_list(request):
    if request.GET:
        get = request.GET
        courses_list = get['course_id']
        students = Student.objects.all()
    else:
        courses_list = 'NO'
        students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students, 'student_courses': Course.objects.all(),
                                                 'courses_list': courses_list})


def add_student(request):

#    model_form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)


        new_student = form.save()
        messages.success(request, 'Form saved')
        return redirect ('/student_list/add/')
    else:
        form = StudentModelForm()

    return render(request, 'add.html', {'model_form': form})

class StudentDetailView(DetailView):

    model = Student
    context_object_name = "student_details"
    # template_name = ""
#    context_object_name = "student_details"


#def student_detail(request):
#    return render(request, 'students/student_detail.html')