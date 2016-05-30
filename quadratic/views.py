# -*- coding: utf-8 -*-

from django.shortcuts import render
import math


def quadratic_results(request):

    if request.GET:

        disc = {}
        disc_result = {}
        valid_data = []
        valid_data_text = None

        def validation(x):

            if x == "":
                valid_data_text = "коэффициент не определен"

            else:
                try:
                    x = int(x)
                    if isinstance(x, int):
                        valid_data.append(x)
                        valid_data_text = ''
                except ValueError:
                    x = str(x)
                    valid_data_text = "коэффициент не целое число"
            return x, valid_data_text

        if request.method == "GET":
            a = request.GET['a']
            b = request.GET['b']
            c = request.GET['c']

            a, a_text = validation(a)
            b, b_text = validation(b)
            c, c_text = validation(c)

            if a == 0:
                a_text = """коэффициент при первом слагаемом
                уравнения, не может быть равным нулю"""

            if len(valid_data) == 3 and a != 0:
                disc['message'] = "Дискриминант: "
                disc['value'] = b**2-4*a*c

                if disc['value'] < 0:
                    disc_result['message'] = '''Дискриминант меньше нуля, квадратное
                    уравнение не имеет действительных решений.'''

                elif disc['value'] == 0:
                    x = -b / (2 * a)
                    disc_result['message'] = '''Дискриминант равен нулю, квадратное
                    уравнение имеет один действительный корень: x1 = x2 = '''
                    disc_result['value'] = float(x)

                elif disc['value'] > 0:
                    x1 = (-b + math.sqrt(disc['value'])) / (2 * a)
                    x2 = (-b - math.sqrt(disc['value'])) / (2 * a)
                    disc_result['message'] = '''Квадратное уравнение имеет два
                    действительных корня: '''
                    disc_result['value'] = "x1 = %.1f, x2 = %.1f" % (x1, x2)

        context = {
            'disc': disc,
            'disc_result': disc_result,
            'a': a, 'a_text': a_text,
            'b': b, 'b_text': b_text,
            'c': c, 'c_text': c_text}

        return render(request, 'quadratic/results.html', context)

    else:
        context = {
            'eq_page': "Квадратное уравнение a*x*x + b*x + c = 0",
            'info': '''Для произведения вычислений, добавьте значения
            коэффициентов в строку URL в формате: ?a=1&b=3&c=5'''}
        return render(request, 'quadratic/results.html', context)
