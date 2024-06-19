# solve quadratic equation 
import cmath

# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

a = 1
b = 5
c = 6

# calculate the discriminant
dis = (b**2) - (4*a*c)

# thera are two solution 
# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
sol1 = (-b + cmath.sqrt(dis))/2*a
sol2 = (-b - cmath.sqrt(dis))/2*a

print('The solution are {0} and {1}'.format(sol1 , sol2))
