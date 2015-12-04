from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})

def list_view(request):
    if 'course_id' in request.GET:
        students = Student.objects.filter(courses=request.GET['course_id'])
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def create(request):
    #form = StudentModelForm()
    res={}   
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            data = form.cleaned_data
            messages.success(request, 'Student %s %s has been successfully added.' % (
                student.name, student.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm() 
    res['form'] = form
    return render(request, 'students/add.html', res)
    
def edit(request, pk):
    form = StudentModelForm()
    student = Student.objects.get(id=pk)
    res={}   
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, 'Info on the student has been successfully changed.')
            
    else:
        form = StudentModelForm(instance = student) 
    res['form'] = form
    return render(request, 'students/edit.html', res)

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (
            student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})
        
