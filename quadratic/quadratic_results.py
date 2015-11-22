from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def results(request):
    #return HttpResponse("Hello, it is results - quadratic.")
    #return render(request, 'results.html')

def results(request):
    eq_ans = int(request.GET['a']) + int(request.GET['b']) + int(request.GET['c'])
    #eq_ans = 'Result {0}'.format(s)
    #return HttpResponse(eq_ans)
    sl = {'sl': eq_ans}
    return render(request, 'results.html', sl)