import sys

import matplotlib
import numpy as np
from math import e, log
from matplotlib import pyplot as plt


def f(x, y):
    global last_y
    try:
        last_y = (y ** 2) * (e ** x) + 2 * y
        return last_y
    except OverflowError:
        return last_y


def euler_method():
    print("Euler")
    i = 0
    while i < n - 1 and y[i] < sys.float_info.max:
        # and x[i] <= epsilon1
        print(i, ")", x[i], y[i])
        try:
            y[i + 1] = y[i] + h * f(x[i], y[i])
        except OverflowError:
            pass
        i += 1
    print(i, ") Euler answer at", x[n - 1], ":", y[n - 1])


def improved_euler():
    print("Improved Euler")
    i = 0
    global y_improved
    while i < n - 1 and y_improved[i] < sys.float_info.max:
        # and x[i] <= epsilon1
        print(i, ")", x[i], y_improved[i])
        k1i = f(x[i], y_improved[i])
        k2i = f(x[i] + h, y_improved[i] + h * k1i)
        print(k1i, k2i)
        try:
            y_improved[i + 1] = y_improved[i] + h * (k1i + k2i) / 2
        except OverflowError:
            pass
        i += 1
    print("Improved Euler answer:", y_improved[n - 1])


def runge_kutta():
    print("Runge-Kutta!")
    i = 0
    while i < n - 1 and y_runge_kutta[i] < sys.float_info.max:
        # and x[i] <= epsilon1
        print(i, ")", x[i], y_runge_kutta[i])
        k1i = f(x[i], y_runge_kutta[i])
        k2i = f(x[i] + h / 2, y_runge_kutta[i] + h * k1i / 2)
        k3i = f(x[i] + h / 2, y_runge_kutta[i] + h * k2i / 2)
        k4i = f(x[i] + h, y_runge_kutta[i] + h * k3i)
        try:
            y_runge_kutta[i + 1] = y_runge_kutta[i] + h * (k1i + 2 * k2i + 2 * k3i + k4i) / 6
        except OverflowError:
            pass
        i += 1
    print("Runge-Kutta answer:", y_runge_kutta[n - 1])


def exact_solution():
    print("c =", c)
    for i in range(n - 1):
        y_exact[i] = ((-3.0) * e ** (2.0 * x[i])) / (
                c + e ** (3.0 * x[i]))
        print(x[i], y_exact[i])
    print("Exact solution at", x[n - 1], ":", y_exact[n - 1])

n = 5
x, y, y_exact, y_improved, y_runge_kutta = [0.0] * n, [0.0] * n, [0.0] * n, [0.0] * n, [0.0] * n
# x[0], y[0], X = 1.0, 0.5, 1.3
x[0], y[0], X = 1.6, -1.289138015374262, 7
h = (X - x[0]) / n
print("h (aka step) =", h)
for i in range(n - 1):
    x[i + 1] = x[i] + h

y_exact[0] = y[0]
y_improved[0] = y_exact[0]
y_runge_kutta[0] = y_exact[0]
last_y = y_exact[0]
c = e ** (2.0 * x[0]) * (-3.0) / y[0] - e ** (
        3.0 * x[0])
asymptote = (1 / 3) * (log(-c, e))
print("vertical asymptote at x = ", asymptote)

epsilon1 = asymptote - h / 2
epsilon2 = asymptote + h / 2
print("eps", epsilon1, epsilon2)

exact_solution()
euler_method()
improved_euler()
runge_kutta()

plt.plot(x, y_exact, 'b')
plt.plot(x, y, 'g')
plt.plot(x, y_improved, 'c')
plt.plot(x, y_runge_kutta, 'm')
print(f(0, 0))
plt.show()
