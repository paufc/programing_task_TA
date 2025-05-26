import matplotlib.pyplot as plt
p = 1.225/3
psl =1.225
S = 27
m = 5100
mfuel = 1020
W = m*9.81
Cdo = 0.019
k = 0.11
v = 40
X = (2*W)/(p*S)
i = 40
Clendurance = (3*Cdo/k)**(1/2)
Cdendurance = Cdo + k*(Clendurance**2)
minimumdrag = ((Clendurance)**(3/2))/Cdendurance
maxefficiency = 1/(2*((Cdo*k)**(1/2)))
Vx = []
Vy = []
while i < 300:
    Vx.append(i)
    a = X/(i**2)
    b = Cdo+k*a**2
    c = a/b
    power = W*i/c
    minimumrequiredpower = ((2**(1/2))*(W**(3/2)))/(((p*S)**(1/2))*minimumdrag)
    minimumrequiredPoverV = W / maxefficiency
    if minimumrequiredpower-100<power<minimumrequiredpower+100:
        xendurance = i
        yendurance = power
    if minimumrequiredPoverV-100< power/i<minimumrequiredPoverV+100:
        xrange = i
        yrange = power
    Vy.append(power)
    i = i + 1
plt.plot(Vx,Vy)
plt.scatter(xendurance, yendurance, color='red', s=50, label = 'maximum endurance')
plt.scatter(xrange, yrange, color='green', s=50, label = 'maximum range')
plt.legend()
plt.title("plot of the airspeed vs the required power")
plt.xlabel("airspeed")
plt.ylabel("required power")
plt.show()
