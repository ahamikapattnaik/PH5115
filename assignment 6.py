#colab or vscode

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#question 1

data = pd.read_excel("/content/projectile.xlsx")  #replace with your file location
t = data['time (s)']
x = data['x(t) in m']
y = data['y(t) in m']

#a
coeff_x = np.polyfit(t, x, 1)
a1, a0 = coeff_x
coeff_y = np.polyfit(t, y, 2)
b2, b1, b0 = coeff_y
x_fit = np.polyval(coeff_x, t)
y_fit = np.polyval(coeff_y, t)

#b
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].scatter(t, x, label='Data', color='blue')
ax[0].plot(t, x_fit, label='Fit: x(t)', color='red')
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Horizontal Position')
ax[0].set_title('Horizontal Motion')
ax[0].legend()
ax[0].grid(True)

ax[1].scatter(t, y, label='Data', color='red')
ax[1].plot(t, y_fit, label='Fit: y(t)', color='blue')
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('Vertical Position')
ax[1].set_title('Vertical Motion')
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()

print(f"Equation of horizontal motion: x(t) = {a1}*t + {a0}")
print(f"Equation of vertical motion: y(t) = {b2}*t² + {b1}*t + {b0}")

#c
distance = a0
print(f"\nDistance between observatory and building: {distance} m")

#d
vx0 = a1
vy0 = b1
print(f"Initial horizontal velocity: {vx0} m/s")
print(f"Initial vertical velocity: {vy0} m/s")

#e
roots = np.roots([b2, b1, b0])
t_flight = np.max(roots)
print(f"Total time of flight: {t_flight} s")

#f
x_final = a1 * t_flight + a0
print(f"Total horizontal distance traveled: {x_final} m")

#question 2

#a
data = pd.read_excel("weightedfit.xlsx")
x = data['x']
y = data['y']
w = data['w']

#b
coeff = np.polyfit(x, y, 2, w=w)
a2, a1, a0 = coeff
y_fit = np.polyval(coeff, x)

#c
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_fit, color='red', label='Weighted Quadratic Fit')
plt.title("Weighted Least Squares Quadratic Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

print(f"Equation of weighted fit: y = {a2}*x² + {a1}*x + {a0}")
