#!/usr/bin/python
# coding=ISO-8859-5
 
import math

def none_coeff_error_text():
	return u'коэффициент не определен'

def not_integer_number_error_text():
	return u'коэффициент не целое число'

def first_coeff_zero_error_text():
	return u'коэффициент при первом слагаемом уравнения не может быть равным нулю'

def discriminant_less_zero_error_text():
	return u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

def validate_first_param(param):
	res = {}

	if param is None:
		res["error_a"] = none_coeff_error_text()
	else:
		try:
			param_a = float(a)
			res["value_a"] = param_a
			if param_a == 0:
				res["error_a"] = first_coeff_zero_error_text()

		except Exception, e:
			res["error_a"] = not_integer_number_error_text()

	return res

def validate_second_param(param):
	res = {}

	if param is None:
		res["error_b"] = none_coeff_error_text()
	else:
		try:
			param_a = float(a)
			res["value_b"] = param_a

		except Exception, e:
			res["error_b"] = not_integer_number_error_text()

	return res

def validate_third_param(param):
	res = {}

	if param is None:
		res["error_c"] = none_coeff_error_text()
	else:
		try:
			param_a = float(a)
			res["value_c"] = param_a

		except Exception, e:
			res["error_c"] = not_integer_number_error_text()

	return res

def validate_discriminant(d):
	res = {}
	res["value_d"] = d
	if d < 0:
		res["error_d"] = discriminant_less_zero_error_text()

	return res

def calculate(params):
	res = {}
	a = params.get("a")
	b = params.get("b")
	c = params.get("c")

	res_a = validate_first_param(a)
	res_b = validate_second_param(b)
	res_c = validate_third_param(c)

	res.update(res_a)
	res.update(res_b)
	res.update(res_c)

	is_valid_a = res_a["error_a"] is None
	is_valid_b = res_b["error_b"] is None
	is_valid_c = res_c["error_c"] is None

	if is_valid_a and is_valid_b and is_valid_c:
		d = b * b - 4 * a * c

		res_d = validate_discriminant(d)

		res.update(res_d)

		if res_d["error_d"] is None:
			x1 = (-b + sqrt(d))/(2 * a)
			x2 = (-b - sqrt(d))/(2 * a)
			res["x1"] = x1
			res["x2"] = x2
	
	return res

		

	