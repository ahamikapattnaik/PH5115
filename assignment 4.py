#question one

from numpy import *
def is_normal(A):
    A_conj_T = conjugate(A.T)
    return allclose(A @ A_conj_T, A_conj_T @ A)
rows, cols = map(int, input("Enter number of rows and columns: ").split())

if rows != cols:
    print("Matrix must be square to check normality.")
else:
    print(f"Enter {rows*cols} elements:")
    elements = [complex(x) for x in input().split()]
    A = array(elements).reshape(rows, cols)
    print("\nMatrix A:")
    print(A)

    if is_normal(A):
        print("The matrix is normal.")
    else:
        print("The matrix is not normal.")

#question two

from numpy import *
def is_unitary(U):
    U_conj_T = conjugate(U.T)
    I = eye(U.shape[0])
    return allclose(U @ U_conj_T, I) and allclose(U_conj_T @ U, I)

rows, cols = map(int, input("Enter number of rows and columns: ").split())
if rows != cols:
    print("Matrix must be square to check unitarity.")
else:
    print(f"Enter {rows*cols} elements:")
    elements = [complex(x) for x in input().split()]
    U = array(elements).reshape(rows, cols)
    print("\nMatrix U:")
    print(U)

    if is_unitary(U):
        print("The matrix is unitary.")
    else:
        print("The matrix is not unitary.")
