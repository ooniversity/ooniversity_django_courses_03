# -*- coding: utf-8 -*
from django.contrib import messages
from django.shortcuts import render, redirect

from students.forms import StudentModelForm
from students.models import Student


# from courses.models import Course


# class StudentApplyForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(label='Mail', help_text='personal email')
#     package = forms.ChoiceField(choices=(
#         ('standart', 'standart'),
#         ('gold', 'Gold'),
#         ('vip', 'VIP')),
#         widget=forms.RadioSelect, initial='standart')
#     news_subscribe = forms.BooleanField(required=False)


# class CourseApplicationForm(forms.ModelForm):

#     class Meta:
#         model = CourseApplication
#         exclude = ['comment', 'is_active']
#         widgets = {'package': forms.RadioSelect}
#         labels = {'email': 'Mail'}
#         help_texts = {'email': 'personal email'}


def list_view(request):
    reguest_course = request.GET
    if 'course_id' in reguest_course:
        list_students = Student.objects.filter(
            courses=reguest_course['course_id'])
    else:
        list_students = Student.objects.all()
    return render(request, 'students/list.html', {'list_students': list_students})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    context = {}
    if request.method == "POST":
        context['form'] = form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            data = form.cleaned_data
            messages.success(request, 'Student %s %s has been successfully added.' % (
                student.name, student.surname))
            return redirect('students:list_view')

    else:
        context['form'] = StudentModelForm()
    return render(request, 'students/add.html', context)


def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(
                request, 'Info on the student has been sucessfully changed.')
            # return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (
            student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})

# def apply_to_course(request):
#     if request.method == 'POST':
#         form = CourseApplicationForm(request.POST)
#         if form.is_valid():
#             application = form.save()
#             messages.success(request, 'Form saved!')
#             return redirect('students:course-application')
#     else:
#         form = CourseApplicationForm(
#             initial={'news_subscribe': True})

#     return render(request, 'students/apply.html',
#                   {'form': form})


# def edit_application(request, pk):
#     application = CourseApplication.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CourseApplicationForm(request.POST, instance=application)
#         if form.is_valid():
#             application = form.save()
#             messages.success(request, 'Form saved!')
#             return redirect('students:course-application')
#     else:
#         form = CourseApplicationForm(instance=application)
#     return render(request, 'students/edit_application.html',
#                   {'form': form})


# def delete_application(request, pk):
#     application = CourseApplication.objects.get(id=pk)
#     if request.method == 'POST':
#         application.delete()
#         messages.success(request, 'Object delete saved!')
#         return redirect('students:course-application')
#     return render(request, 'students/delete_application.html',
#         {'application':application})
