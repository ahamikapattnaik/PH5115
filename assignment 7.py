#1
import pandas as pd
import numpy as np

# Read data from Excel file. Excel file has columns named 'x' and 'y'
data = pd.read_excel('data.xlsx')

# Extract x and y columns as numpy arrays
x = data['x'].to_numpy()
y = data['y'].to_numpy()

# Check that data is sorted by x (x may not be sorted in the excel file)
sorted_indices = np.argsort(x)
# argsort gives indices for sorted array. It doesn’t sort the array
x = x[sorted_indices]
y = y[sorted_indices]

# Apply Trapezium rule
integral = np.trapezoid(y, x)

# Print the result
print("Numerical integration result (Trapezium rule):", integral)

#2

import pandas as pd
import numpy as np
from scipy.integrate import simpson

# Read data from Excel assume first column = x, second column = y
data = pd.read_excel('data.xlsx')

x = data['x'].to_numpy()
y = data['y'].to_numpy()

# Simpson function uses 1/3 rd rule for even intervals and 3/8 rule for odd
I_simpson = simpson(y, x)

print(f"Simpson's integration result: {I_simpson:}")


#3
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
V = 5 # supply voltage (volts)
R = 4.763 # resistance (ohms)
C = 1e-6 # capacitance (farads)
q0 = 0 # initial charge (coulombs)
t_end = 0.5 # total simulation time (seconds)
h = R*C/10 # time step (seconds)

# Define dq/dt
def dqdt(q, t):
    return (V - q / C) / R

t = np.arange(0, t_end + h, h)
q = np.zeros(len(t))
q[0] = q0

# Loop for Euler method
for i in range(1, len(t)):
    q[i] = q[i-1] + h * dqdt(q[i-1], t[i-1])

# Plot
plt.plot(t, q, label='Charge across capacitor (by Euler)')
plt.xlabel('Time (s)')
plt.ylabel('Capacitor Charge (C)')
plt.title('Charging of Capacitor using Euler Method')
plt.grid(True)
plt.legend()
plt.show()

#4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
m = 1.0 # mass
c = 0.2 # damping
k = 4.0 # force constant
F0 = 1.0 # driving amplitude
omega = 1.5 # driving frequency

t0 = 0.0 # start time
tf = 20.0 # end time
h = 0.01 # time step
t = np.arange(t0, tf + h, h) # time array

x0 = 0.0 # initial value x(0)=0
v0 = 0.0 # we use v for x', initial value x'(0)=v(0)=0

def accel(x, v, time): # function for acceleration a
    return (1.0/m) * (F0 * np.cos(omega * time) - c * v - k * x)

# Euler method
x_e = np.zeros(len(t)) # x array
v_e = np.zeros(len(t)) # v array
x_e[0] = x0 # first value
v_e[0] = v0 # first value

for n in range(len(t) - 1):
    x_e[n+1] = x_e[n] + h * v_e[n]
    v_e[n+1] = v_e[n] + h * accel(x_e[n], v_e[n], t[n])

# Plots
plt.figure(figsize=(10, 4))
plt.plot(t, x_e, label='Euler x(t)')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.title('Displacement vs Time')
plt.legend()
plt.grid(True)
plt.show()


#5 
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0 # Width of the potential well
N = 1000 # Number of grid points
x = np.linspace(0, L, N)
h = x[1] - x[0] # Step size

# Function to compute psi for a given quantum number n
def wavefunction(n):
    psi = np.zeros(N)
    psi[0] = 0 # boundary condition psi(0) = 0
    psi[1] = 1e-5 # small starting value at psi(1)

    for i in range(2, N):
        psi[i] = (2 - (n * np.pi * h / L)**2) * psi[i-1] - psi[i-2]

    # Normalize
    psi /= np.sqrt(np.trapz(psi**2, x))  
    # find integral of psi^2 then divide each psi value by this integral
    return psi

# Plot the first three wavefunctions
for n in range(1, 4):
    psi = wavefunction(n)
    plt.plot(x, psi, label=f'n={n}')

plt.title("Wavefunctions of a Particle in a 1D Infinite Potential Well")
plt.xlabel("x (position)")
plt.ylabel("psi(x)")
plt.legend()
plt.grid(True)
plt.show()
