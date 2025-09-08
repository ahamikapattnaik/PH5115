#q1: refer 'part two.py'

#q2:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

primes = [num for num in range(start, end + 1) if is_prime(num)==True]

print(f"Prime numbers between {start} and {end} are:")
print(primes)

#q3: pickle
import pickle

data = input("Enter average daily temperatures for 7 days (separated by commas): ")
temp = [float(x) for x in data.split(",")] 

f= open("tempdata1.dat", "wb")
pickle.dump(temp, f)
f.close()

f= open("tempdata1.dat", "rb")
newtemp1 = pickle.load(f)
print("Temperature data read from file:", newtemp1)
f.close()

minimum = min(newtemp1)
maximum = max(newtemp1)
average = sum(newtemp1) / len(newtemp1)

print("\nWeekly Temperature Report")
print("Minimum temperature:", minimum)
print("Maximum temperature:", maximum)
print("Average temperature:", average)
