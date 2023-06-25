#!/usr/bin/python3
import calculator_1

a = 10
b = 5

result_add = calculator_1.add(a, b)
result_subtract = calculator_1.subtract(a, b)
result_multiply = calculator_1.multiply(a, b)
result_divide = calculator_1.divide(a, b)

print("The sum of {} and {} is {}".format(a, b, result_add))
print("The difference between {} and {} is {}".format(a, b, result_subtract))
print("The product of {} and {} is {}".format(a, b, result_multiply))
print("The division of {} by {} is {}".format(a, b, result_divide))
