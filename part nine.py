#Generate Pseudo-Random Numbers
import numpy as np
seed = 1
rng = np.random.default_rng(seed)
r_numbers = rng.random(10)
print(r_numbers)
r_integers =  rng.integers(0,100,10)
print(r_integers)

#Generating Random Numbers, seed = none
rng = np.random.default_rng(None)
r_numbers = rng.random(10)
print(r_numbers)
r_integers = rng.integers(0,100,10)
print(r_integers)

#Crude Integration
rng = np.random.default_rng(1)
def f(x):
    return x*np.sin(x)
a,b = -1,1
x = rng.uniform(a,b,1000000)  #N=1000000
fx = f(x)
I = (b-a)*np.mean(fx)
print(I)
##--alternate way--
rng = np.random.default_rng(1)
def I(f, a, b, N):
    x = rng.uniform(a, b, N)
    return (b-a) * np.mean(f)
I = I(x*np.sin(x),-1,1,1000000)
print(I)

#Importance Sampling
a,b = -0.99,0.99   #reduce interval by neglecting insignificant values
x = rng.uniform(a,b,1000000)
fx = f(x)
I = (b-a)*np.mean(fx)
print(I)

#Radioactive Decay
import numpy as np
import matplotlib.plt as plt
rng=np.random.default_rng(0)
N = 10000
decayprob = 0.05
sim_time = 50

nuclei = np.ones(N, dtype=int)
survived = []
survived.append(np.sum(nuclei))

for t in range(sim_time):
    decay_events = rng.random(N) < decayprob
    nuclei[decay_events] = 0
    survived.append(np.sum(nuclei))

plt.plot(survived)
plt.xlabel("Time (s)")
plt.ylabel("Number of undecayed nuclei")
plt.title("Monte Carlo Simulation of Radioactive Decay")
plt.show()

#Particle in a Box
import numpy as np; import matplotlib.pyplot as plt
L = 1.0 #length of box
N = 5000 #number of time steps
h = 0.05 #step size
x,y,z = L/2,L/2,L/2 #at centre
xpos,ypos,zpos = np.zeros(N),np.zeros(N),np.zeros(N)
rng=np.random.default_rng()

for i in range (N):
    dx,dy,dz = rng.uniform(-h,h),rng.uniform(-h,h),rng.uniform(-h,h)
    x = x+dx
    y = y+dy
    z = z+dz

    if x<0:
        x = -x
    elif x>L:
        x = L - (x-L)
    if y<0:
        y = -y
    elif y>L:
        y = L - (y-L)
    if z<0:
        z = -z
    elif z>L:
        z = L - (z-L)

    xpos[i]=x
    ypos[i]=y
    zpos[i]=z

fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot(xpos,ypos,zpos,color='b')
ax.scatter(xpos[0],ypos[0],zpos[0],color='y',s=50,label='start')
ax.scatter(xpos[N-1],ypos[N-1],zpos[N-1],color='r',s=50,label='stop')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()
