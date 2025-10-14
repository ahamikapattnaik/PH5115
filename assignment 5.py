#question 1
pip install pandas openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

data = pd.read_excel("/content/HR_diagram_data.xlsx")
T = data['Temperature (K)']
L = data['Luminosity (Lsun)']
norm_T = (T - T.min()) / (T.max() - T.min())

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(T, L, c=cm.RdYlBu(norm_T))
ax.set_yscale("log")
ax.invert_xaxis()

ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Luminosity (Lsun)")
ax.set_title("H-R Diagram with Temperature-Based Colours")

ax.text(0.5, 0.5, "Main Sequence", transform=ax.transAxes, color='blue')
ax.text(0.75, 0.95, "Red Giants", transform=ax.transAxes, color='red')
ax.text(0.1, 0.1, "White Dwarfs", transform=ax.transAxes, color='purple')

plt.show()

#question 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn

x = np.linspace(0, 20, 400)
plt.figure(figsize=(12,8))

for n in range(4):
    plt.plot(x, jn(n, x), label=f'J{n}(x)')

plt.xlim(0, 20)
plt.ylim(-0.5, 1)
plt.title("Bessel Functions of the First Kind (Orders 0–3)")
plt.xlabel("x")
plt.ylabel("Jn(x)")
plt.legend()
plt.grid(True)
plt.show()

#question 3
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)
ax.set_title("3D Surface Plot of z = sqrt(x**2 + y**2)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()

#question 4
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 800)
r = np.abs(np.sin(5 * theta))

ax = plt.subplot(projection="polar")
ax.plot(theta,r,color="r")
plt.show()
