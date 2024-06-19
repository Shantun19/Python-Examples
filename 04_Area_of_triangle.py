# program to find the area of a triangle.
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

a = float(input('Enter first Side'))
b = float(input('Enter Second Side '))
c = float(input('Enter third Side'))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*((s-c))) ** 0.5
print('The area of a triangle is %0.2f' %area)
