import matplotlib.pyplot as plt

v = 40
Vx = []
Vy = []
while v < 300:
    Vx.append(v)
    a = 9075/v**2
    b = 0.019+0.11*a**2
    c = a/b
    thrust = 50031/c
    if 4570<thrust<4576:
        x = v
        y = thrust

    Vy.append(thrust)
    v = v + 1

plt.plot(Vx,Vy)
plt.scatter(x, y, color='red', s=50)
plt.title("plot of the airspeed vs the required thrust")
plt.xlabel("airspeed")
plt.ylabel("required thrust")
plt.show()