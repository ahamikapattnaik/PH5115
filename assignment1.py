#q1 easy, skip

#q2: refer 'part one.py'

#q3: roots of quadratic eqn using cmath, sqrt(), and take values from user
from cmath import sqrt
print("Quadratic Equation is of the form \n a*(x**2) + b*x + c")
a,b,c = map(float,input("Enter a,b,c separated by a comma: ").split(","))
root1 = (-b + sqrt((b**2)-4*a*c))/(2*a)
root2 = (-b - sqrt((b**2)-4*a*c))/(2*a)
print(f"The roots are {root1} and {root2}")

#q4 easy, skip

#q5: check types
#example
a=3
print(a,type(a))
b=3.4
print(b,type(b))
c='hello'
print(c,type(c))
d=5-9j
print(d,type(d))
