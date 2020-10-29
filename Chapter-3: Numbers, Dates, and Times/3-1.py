'''
Rounding Numerical Values
Problem: You want to round a floating-point number to a fixed number of decimal place.
'''

print(round(1.23, 1))
print(round(1.27, 1))

a = 1627731
print(round(a, -1))
# for the below python will always try to
# round it to closest even number.
print(round(1.5, 0))
print(round(2.5, 0))