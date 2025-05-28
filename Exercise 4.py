from data import*
import matplotlib.pyplot as plt
import numpy as np

def foundROD(airspeed):
    global m, g, A, B
    requiredThrustAMBspeed=(A*partialDensityAtCR*airspeed**2)+((B*(m*g)**2)/(airspeed**2*partialDensityAtCR))
    ROD=-(requiredThrustAMBspeed*airspeed)/(m*g)
    return ROD

airspeeds=range(75,250,1)
RODs=[]

for speeds in airspeeds:
    a=foundROD(speeds)
    RODs.append(a)
GLIDEs=[]
i=0
while i<len(airspeeds):
    glide_ratio=airspeeds[i]/abs(RODs[i])
    GLIDEs.append(glide_ratio)
    i=i+1

max_index=np.argmax(GLIDEs)
best_speed=airspeeds[max_index]
best_ROD=RODs[max_index]

i=0
max_value=RODs[0]
while i<len(RODs): #trobar glide time max
    if max_value<RODs[i]:
        max_value=RODs[i]
        max_speed=airspeeds[i]
    i=i+1
print(best_speed)

plt.plot(airspeeds,RODs)
plt.grid()
plt.xlabel("Airspeed [m/s]")
plt.ylabel("Sink Rate [m/s]")
plt.title("Airspeed vs Sink Rate")
plt.scatter(best_speed, best_ROD, color='red', label='Maximimum glide distance')
plt.scatter(max_speed, max_value, color='green', label='Maximum glide time')
plt.legend()
plt.show()