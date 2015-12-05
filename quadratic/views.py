#-*-coding: utf-8-*-
from django.conf.urls import patterns, include, url
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from forms import QuadraticForm


def quadratic_results(request):
    if request.method == "GET":
        form = QuadraticForm(request.GET)


        #print form
        #print type(form)
        
        context = {'form': form}
        
        # this if made for chosing table or just rendering for        
        if form.is_valid():
            a = int(form['a'].value())
            b = int(form['b'].value())
            c = int(form['c'].value())

            # Calculate discriminant
            discr = b * b - 4 * a * c
            
            if discr == 0:
                x1 = - b / (2.0 * a)
                x1 = round(x1, 1)
                discr_msg = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0}".format(x1)

            elif discr < 0:
                discr_msg = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."

            else:
                x1 = (- b + discr ** (1/2.0)) / (2 * a)
                x2 = (- b - discr ** (1/2.0)) / (2 * a)
                x1 = round(x1, 1)
                x2 = round(x2, 1)
                round(x1, 1)
                discr_msg = "Квадратное уравнение имеет два действительных корня: x1 = {0}, x2 = {1}".format(x1, x2)
            context['discr_msg'] = discr_msg
            context['discr'] = discr
        

        elif form['a'].value() == form['b'].value() == form['c'].value() == None:
            context['form'] = QuadraticForm()

    return render(request, 'results.html', context)