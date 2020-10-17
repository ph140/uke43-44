from matplotlib import pyplot as plt
import numpy as np
import math


def sinus(x):
    return math.sin(x)


def tangens(x):
    return math.tan(x)


def cosinus(x):
    return math.cos(x)


def polynom(x):
    return (x**2/10) - 2*x + 5


def visgraf(funksjon):
    steglengde = 0.1
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


visgraf(sinus)
visgraf(tangens)
visgraf(cosinus)
visgraf(polynom)
