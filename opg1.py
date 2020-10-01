from matplotlib import pyplot as plt
import numpy as np
import math


def sinFunksjon(x):
    return math.sin(x)


def tanFunksjon(x):
    return math.tan(x)


def cosFunksjon(x):
    return math.cos(x)


def polFunksjon(x):
    return (x**2/10) - 2*x + 5


def visgraf(funksjon, steglengde):
    xverdier = []
    yverdier = []
    firePi = int((4*math.pi)/steglengde)
    for i in range(firePi):
        if i*steglengde > math.pi * 4:
            break

        xverdier.append(i*steglengde)

    for x in xverdier:
        yverdier.append(funksjon(x))

    plt.plot(xverdier, yverdier, 'b--')
    plt.xlabel("x-akse")
    plt.ylabel("y-akse")
    plt.title(str(funksjon))

    plt.ylim(-10, 10)
    plt.show()


visgraf(sinFunksjon, 0.0001)
visgraf(tanFunksjon, 0.0001)
visgraf(cosFunksjon, 0.0001)
visgraf(polFunksjon, 0.0001)

dajgajglkdgjkøj
dajgajglkdgjkøj
dajgajglkdgjkøj


dajgajglkdgjkøj
dajgajglkdgjkøj
dajgajglkdgjkøj
dajgajglkdgjkøj
dajgajglkdgjkøj
dajgajglkdgjkøj
dajgajglkdgjkøj
dajgajglkdgjkøj
