from utils import input_parameter, get_discr
print "enter coefficient"
a = input_parameter()
b = input_parameter('b')
c = input_parameter('c')
d = get_discr(a, b, c)

if d < 0:
	print "Root of the equation dows not exist"
	exit()
elif d == 0:
	x = -b / 2*a
	print "This is one equation root x1=x2=%g" %x
else:
	x1 = (-b + d ** (1/2.0)) / (2*a)
	x2 = (-b - d ** (1/2.0)) / (2*a)
	print "There are roots of equation x1=%g, x2=%g" % (x1, x2)	