# -*- coding: utf-8 -*-
from math import sqrt


class QuadraticEquation(object):
    def analyze(self, key):
        if self.data[key]:
            try:
                self.data[key] = int(self.data[key])
                if self.data[key] == 0 and key == 'a':
                    self.errors[key] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
                    self.has_error = True
            except:
                self.errors[key] = 'коэффициент не целое число'
                self.has_error = True
        else:
            self.errors[key] = 'коэффициент не определен'
            self.has_error = True

    def __init__(self, data):
        self.data = data
        self.has_error = False
        self.errors = {}
        self.result = {'description': None, 'x1': None, 'x2': None}
        self.analyze('a')
        self.analyze('b')
        self.analyze('c')
        self.solve()

    def solve(self):
        if not self.has_error:
            a = self.data['a']
            b = self.data['b']
            c = self.data['c']
            self.data['d'] = b * b - 4 * a * c
            if self.data['d'] < 0:
                self.result[
                    'description'] = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif self.data['d'] == 0:
                self.result[
                    'description'] = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:'
                self.result['x1'] = str(format(- b / 2.0 / a, '.2f'))
            elif self.data['d'] > 0:
                self.result['description'] = 'Квадратное уравнение имеет два действительных корня:'
                self.result['x1'] = (-b + sqrt(self.data['d'])) / 2.0 / a
                self.result['x2'] = (-b - sqrt(self.data['d'])) / 2.0 / a
