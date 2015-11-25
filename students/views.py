from django.shortcuts import render
from django.http import HttpResponse
#from courses.models import Course, Lesson
from students.models import Student

"""
def list_view(request, course_id = None):
    #return HttpResponse('course={}'.format(course_id))
    args = {}
    if course_id == None:
        st = Student.objects.all()
        args['students'] = st


    else:
        st = Student.objects.filter(courses__id=course_id)
        args['students'] = st
    
    return render(request, 'students/list.html', args)
"""

def list_view(request):
    #return HttpResponse('course={}'.format(course_id))
    #print course_id
    #print request.GET
    args = {}
    #a = request.GET.keys()
    #try: 
        #st = Student.objects.filter(courses__id=request.GET['course_id'])
        #args['students'] = st
        
        
    

        
    #except:
     
    if  request.GET.get('course_id'): 
        course = request.GET.get('course_id')
        st = Student.objects.filter(courses=course)
        args['students'] = st    
    else:
                 
        st = Student.objects.all()
        args['students'] = st
    
        
    
    return render(request, 'students/list.html', args)

def detail(request, stud_id):
    #print stud_id
    args={}
    args['stud_id'] = stud_id
    st = Student.objects.get(id=stud_id)
    args['student'] = st
    #return HttpResponse('student={}'.format(stud_id))
    return render(request, 'students/detail.html', args)
        


