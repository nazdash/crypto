# AMM machine

import matplotlib as mpl

mpl.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# defining pool
x = 0.0
y = 0.0
t = 0
period = []
price = []
volume = []
xq = float(input("Enter initial token X quantity in a pool: "))
xp = float(input("Enter initial token X price in $: "))
yp = float(input("Enter initial token Y price in $: "))
yq = xq * xp / yp
p = xq * xp  # half-pool price
s = xq + yq
k = xq * yq
print("Initial token Y quantity in a pool:", yq)
print("X token share in a pool:", xq / s)
print("Y token share in a pool:", yq / s)
print("Price ratio:", xp / yp)
print("s =", s)
print("k =", k)
print("")
period.append(t)
price.append(xp / yp)
#volume.append(0)
plt.plot(period, price, volume)
plt.savefig('graph.png')

i = 0
while i == 0:

    exc_token = input("Select token you want to exchange (X or Y): ")

    if exc_token.lower() == 'x':
        q = float(input("Enter number of tokens you want to exchange: "))
        xq = xq + q
        y = k / xq
        yqr = yq - y
        yq = y
        print("Y received:", yqr)
    elif exc_token.lower() == 'y':
        q = float(input("Enter number of tokens you want to exchange: "))
        yq = yq + q
        x = k / yq
        xqr = xq - x
        xq = x
        print("X received:", xqr)
    else:
        print("Invalid token")

    xp = p / xq
    yp = p / yq
    s = xq + yq
    k = xq * yq
    print("X quantity in a pool =", xq)
    print("Y quantity in a pool =", yq)
    print("X price:", xp)
    print("Y price:", yp)
    print("X token share in a pool:", xq / s)
    print("Y token share in a pool:", yq / s)
    print("Price ratio:", xp / yp)
    print("s =", s)
    print("k =", k)
    print("")

    t += 1
    period.append(t)
    price.append(xp / yp)
    #volume.append(q*xp)
    plt.plot(period, price)
    plt.savefig('graph.png')
