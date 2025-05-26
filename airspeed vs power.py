import matplotlib.pyplot as plt

i = 40
Vx = []
Vy = []
while i < 300:
    Vx.append(i)
    a = 9075/i**2
    b = 0.019+0.11*a**2
    c = a/b
    power = 50031*i/c
    if 590000<power<600000:
        x = i
        y = power
    Vy.append(power)
    i = i + 1

plt.plot(Vx,Vy)
plt.scatter(x, y, color='red', s=50)
plt.title("plot of the airspeed vs the required thrust")
plt.xlabel("airspeed")
plt.ylabel("required power")
plt.show()