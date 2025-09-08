from numpy import *

#array using NumPy
a = array([1,2,3,5])
print(a, type(a))

#2D arrays
a = array([[1,2],[3,5]])
print(a, type(a))

#3D arrays
a = array([[[0,4],[8,9]],[[1,2],[3,5]]])
print(a, type(a))
print("shape=",a.shape)
print("dimension=",a.ndim)

#arange NOT ARRANGE, linspace
x = arange(2,20,3)
print(x)

y = linspace(2,20,3)
print(y)

#zeros, ones, and full; shape should be tuple
o=zeros((4,5))
print(o)

i=ones((4,5))
print(i)

f=full((4,5),7,int)
print(f)

#diagonal matrix
I = eye(3)
print(I)

A = eye(3,3)
print(A)

I2= I*5
print(I2)

K1= eye(3,4,2)
print(K1)

K_1 = eye(3,4,-2)
print(K_1)

#C and F order
a=arange(12)
a1=a.reshape((3,4), order='C')
print(a1)
a2=a.reshape((3,4), order='F')
print(a2)

#stacking
a=array([1,2,3])
b=array([4,5,6])
c=column_stack((a,b))
r=vstack((a,b))
print(c,'\n \n',r)

#create an array of odd numbers between 1 and 20
odd=arange(1,20,2)
print(odd)

#generate a 5x5 matrix filled with 7
I=identity(5)
print(I*7)

#Generate 10 numbers between 0 and 2pi, and reshape into 5x2
a=linspace(0,2*pi,10)
a=a.reshape(5,2)
print(a)
