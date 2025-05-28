from data import*
import matplotlib.pyplot as plt
import numpy as np

def foundROD(airspeed):
    global m, g, A, B
    requiredThrustAMBspeed=(A*partialDensityAtCR*airspeed**2)+((B*(m*g)**2)/(airspeed**2*partialDensityAtCR))
    ROD=-(requiredThrustAMBspeed*airspeed)/(m*g)
    return ROD

def foundGlideAngle(airspeed):
    sink_rate = abs(foundROD(airspeed))
    angle_rad = np.arctan(sink_rate / airspeed)
    angle_deg = -np.degrees(angle_rad)
    return angle_deg


airspeeds = range(75, 250, 1)
ANGLEs = [foundGlideAngle(v) for v in airspeeds]

best_angle=ANGLEs[0]

for angle in ANGLEs:
    if best_angle<angle:
        best_angle=angle
best_angle=np.radians(best_angle)
liftTOdrag=1/-np.tan(best_angle)
print(liftTOdrag)

plt.plot(airspeeds, ANGLEs)
plt.grid()
plt.title("Airspeed vs Min Glide Angle")
plt.xlabel("Airspeed [m/s]")
plt.ylabel("Glide Angle [degrees]")
plt.title("Airspeed vs Glide Angle")
plt.show()