from data import *
import numpy as np
b=ThrustAvailableAtSL
a=getThrust(partialDensityAtCR)

v=25/1.944




#MAX AOC dont depebds on speed
airspeed=148+v
AOC=np.degrees(np.arcsin((a-(A*partialDensityAtCR*airspeed**2)+((B*(m*g)**2)/(airspeed**2*partialDensityAtCR)))/(m*g)))
print("max aoc,",AOC)
airspeed=148-v
AOC=np.degrees(np.arcsin((a-(A*partialDensityAtCR*airspeed**2)+((B*(m*g)**2)/(airspeed**2*partialDensityAtCR)))/(m*g)))
print("max aoc,",AOC)

#MIN DESCENT ANGLE
airspeed=148+v
c=(A*partialDensityAtCR*airspeed**2)+((B*(m*g)**2)/(airspeed**2*partialDensityAtCR))
minSINK=np.degrees(-np.arcsin(c/(m*g)))
print("min glide angle tailwind,", minSINK)

airspeed=148-(25/1.944)
c=(A*partialDensityAtCR*airspeed**2)+((B*(m*g)**2)/(airspeed**2*partialDensityAtCR))
minSINK=np.degrees(-np.arcsin(c/(m*g)))
print("min glide angle headwind,", minSINK)

Ejet=0.233
Vjet=91.53

Eprop=0.00172
Vprop=112.26

Rjet1=Ejet*(Vjet+v)
Rjet2=Ejet*(Vjet-v)
print(f"Turbojet: with headwind {Rjet2}m and with tailwind {Rjet1}m ")

Rprop1=Eprop*(Vprop+v)
Rprop2=Eprop*(Vprop-v)
print(f"Turboprop: with headwind {Rprop2}m and with tailwind {Rprop1}m ")
