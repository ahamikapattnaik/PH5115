#while loop
num=int(input("Enter a non negative integer"))
while num>=0:
  print(num)
  num = num-1

#factorial using while
n=int(input("Enter an integer: "))
f=1
while n>1:
  f=f*n
  n=n-1
print("The factorial is:",f)

#for loop
for i in range(10):
  print(i)
for i in range(2,7):
  print(i)
for i in range(1,10,2):
  print(i)

#factorial using if, else, for
n=int(input("Enter an integer"))
f=1
if n>1:
    for i in range(2,n+1):
        f=f*i
print("factorial is: ",f)

#user defined functions
def sayhello(n):
  n=int(n)
  s='Hello...'*n
  print(s)
sayhello(3)

#factorial using def
def fact(n):
  if n<=1:
    return 1
  else:
    return n*fact(n-1)
n=int(input("Enter an integer: "))
print("The factorial is: ", fact(n))

'''
COMMENT: OPENING AND CLOSING A FILE

f=open("file location.txt", "w") #opens a file in writing mode
f.write('enter your string')
f.close() #closes the file

f=open("file location.txt", "r") #opens a file in reading mode
print(f.read()) #will print the entire of it, you can use optional variable to specify number of characters
f.close()

f=open("file location.txt", "a") #opens a file in append mode
f.write('enter your second string')
f.close()

f=open("file location.txt", "r") #opens a file in reading mode
print(f.read()) #will print the entire of it, you can use optional variable to specify number of characters
f.close()
'''

'''
COMMENT: USING PICKLE MODULE

Use 'wb' and 'rb' instead of w and r (for binary stuff)

f.write becomes:
pickle.dump([your list],f)

f.read becomes:
var = pickle.load(f)
print(var)
'''

#exception handling
x=float(input("Enter a number: "))
try:
  print(10/x)
except:
  print("Error")
