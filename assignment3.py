#q1

#a
from numpy import *
even=arange(2,20,2)
print("The even numbers between 1 and 20 are: ",even)

#b
I=identity(5)
print(I*7)

#c
a=linspace(0,2*pi,10)
a=a.reshape(5,2)
print(a)

#d
M=eye(3,4)
print(M*(1/2))

#q2
from numpy import *
values = list(map(float, input("Enter 9 decimal values separated by spaces: ").split()))
A = array(values).reshape(3, 3)
print("Original A=",A)
B = A ** 2
print("\n Original B=",B)
savez("arrays.npz", A=A, B=B)
C=load("arrays.npz")
print("\n Retrieved A =", C["A"])
print("\n Retrieved B = ", C["B"])

#q3
from numpy import *
A=array([[3,1,-1],[2,-2,4],[-1,1/2,-1]])
B=array([1,-2,0])
X=linalg.solve(A,B)
print("The solutions are: ", X)

#q4
r,c = map(int, input("Enter number of rows and columns separated by space: ").split())
if r!= c:
    print("Matrix must be square to check orthogonality.")
else:
    elements = list(map(float, input(f"Enter {r*c} elements: ").split()))
    A = array(elements).reshape(r, c)
    A_T = A.T
    try:
        A_inv = linalg.inv(A)
        if allclose(A_inv, A_T):
            print("The matrix is orthogonal.")
        else:
            print("The matrix is not orthogonal.")
    except:
        print("Singular matrix cannot be orthogonal.")
