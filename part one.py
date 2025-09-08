#easy peasy lemon squeezy

#area and circumference of a circle
r = 10
pi = 3.14
area = pi*(r**2)
circ = 2*pi*r
print(f"area= {area} , circumference= {circ}")
input("Press any key to exit.")

#taking r from user
r = int(input("Give an integer value for radius"))
pi = 3.14
area = pi*(r**2)
circ = 2*pi*r
print(f"area= {area} , circumference= {circ}")

#splits
s="Hello, How are you?"
s1=s.split()
s2=s.split(",")
print(s1, "\n", s2)

#joining
s="Hello, How are you?"
s1=s.split()
s2=s.split(",")
print("".join(s1))
print("+".join(s2))

#joining example 2
j=['A','h','a','m','i','k','a']
print("".join(j))

#boolean
x=1
y=0
print(f"x= {x} and y= {y}")
print("x and x =", x and x)
print("x and y =", x and y)
print("y and y =", y and y)
print("x or x =", x or x)
print("y or y =", y or y)
print("x or y =", x or y)
print("not x =", not x)

#more operators...
a="Ahamika"
print(a[0])
print(a[3])
print(a[-2])
print(a[3:])
print(a[:2])
print(a[2:5])
print(a.upper())
print(a.lower())

#remove vs del vs pop
c=[1,2,3,4,5,6]
c.remove(3)
print(c)
del c[3]
print(c)
x=c.pop(1)
print(x)

#sets
a={2,3,1,5,9}
b={3,4,5,6,0}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)

#set is mutable BUT APPEND DOESN'T WORK
bleh={8,9,0,1}
bleh.add(3)
print(bleh)
bleh.remove(0)
print(bleh)
bleh.update([-3,2,-5])
print(bleh)

#area of triangle
b,h =  map(float,input("Enter base and height of triangle split by comma: ").split(","))
area = 0.5*b*h
print(area)

#average marks
a,b,c,d = map(float,input("Enter marks separated by space: ").split())
avg = (a+b+c+d)/4
print(avg)

#method 2
a,b,c,d = map(float,input("Enter marks separated by space: ").split())
s= [a,b,c,d]
avg= sum(s)/len(s)
print(avg)
