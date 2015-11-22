class QadraticEquation(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calc_discr(self):
         self._d = self.b ** 2 - 4 * self.a * self.c
    def get_discr(self):
         return self._d
    def get_eq_root(self, order = 1):
        if order==1:
            x = (-self.b + self._d ** (1/2.0)) / 2*self.a
        else:
            x = (-self.b - self._d ** (1/2.0)) / 2*self.a
        return x
def input_parameter(parameter_name = 'a'):
    while True:
        p = raw_input("Enter the parameter for the qadratoric equation: %s = " %parameter_name)
        if p.replace('.', '').replace('-', '').isdigit() and float(p) != 0:
            return float(p)
        else:
            print "Please enter the number of nonzero"
