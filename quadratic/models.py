# -*- coding: utf-8 -*-
from django.db import models

from math import sqrt

class QuadraticCalc(object):

    def __init__(self, data):
        self.data = data
        self.error = False
        self.errors = {}
        self.result = {'description': None, 'x1': None, 'x2' : None}
        self.validation('a')
        self.validation('b')
        self.validation('c')
        self.calculate()

    def validation(self, inpt):
        if self.data[inpt]:
            try:
                self.data[inpt] = int(self.data[inpt])
                if self.data[inpt] == 0 and inpt=='a':
                    self.errors[inpt] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
                    self.error = True
            except:
                self.errors[inpt] = 'коэффициент не целое число'
                self.error = True
        else:
            self.errors[inpt] =  'коэффициент не определен'
            self.error = True

    def calculate(self):
        if not self.error:
            a = self.data['a']
            b = self.data['b']
            c = self.data['c']
            self.data['d'] = b * b - 4 * a * c
            if self.data['d'] < 0:
                self.result['description'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif self.data['d'] == 0:
                self.result['description'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:'
                self.result['x1'] = - b / 2.0 / a
            elif self.data['d'] > 0:
                self.result['description'] = 'Квадратное уравнение имеет два действительных корня:'
                self.result['x1'] = (-b + sqrt(self.data['d']))/ 2.0 / a
                self.result['x2'] = (-b - sqrt(self.data['d']))/ 2.0 / a
