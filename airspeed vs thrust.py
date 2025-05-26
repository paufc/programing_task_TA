import matplotlib.pyplot as plt
from fontTools.misc.py23 import xrange
p = 1.225/3
psl =1.225
S = 27
m = 5100
mfuel = 1020
W = m*9.81
Cdo = 0.019
k = 0.11
v = 40
Vx = []
Vy = []
X = (2*W)/(p*S)
while v < 350:
    Vx.append(v)
    a = X/v**2
    b = Cdo+k*a**2
    c = a/b
    thrust = W/c
    minimumrequiredthrust = (W)/10.93
    A = 0.5*psl*S*Cdo
    B = (2*k)/(psl*S)
    minimumrequiredToverV = (3**(-3/4))*4*(((A**3)*B)**(1/4))*((W*p)**(1/2))
    if (minimumrequiredthrust-100)<thrust<(minimumrequiredthrust+100):
        xendurance = v
        yendurance = thrust
    if minimumrequiredToverV-1<thrust/v<minimumrequiredToverV+1:
        xrange = v
        yrange = thrust

    Vy.append(thrust)
    v = v + 1

plt.plot(Vx,Vy)
plt.scatter(xendurance, yendurance, color='red', s=50, label = 'maximum endurance')
plt.scatter(xrange, yrange, color='green', s=50, label = 'maximum range')
plt.legend()
plt.title("plot of the airspeed vs the required thrust")
plt.xlabel("airspeed")
plt.ylabel("required thrust")
plt.show()
