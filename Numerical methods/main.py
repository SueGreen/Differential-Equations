import sys

import matplotlib
import numpy as np
from math import e, log
from matplotlib import pyplot as plt


class My_function:
    last_value = 0

    def f(self, x, y):
        try:
            self.last_value = (y ** 2) * (e ** x) + 2 * y
            return self.last_value
        except OverflowError:
            return self.last_value


class Euler():
    def euler_method(self):
        print("Euler")
        self.euler_func = [0.0] * n
        self.euler_func[0] = init.exact_func[0]
        i = 0
        while i < n - 1 and self.euler_func[i] < sys.float_info.max:
            # and x[i] <= epsilon1
            print(i, ")", init.x[i], self.euler_func[i])
            try:
                self.euler_func[i + 1] = self.euler_func[i] + init.h * my_funct.f(init.x[i], self.euler_func[i])
            except OverflowError:
                pass
            i += 1
        print(i, ") Euler answer at", init.x[n - 1], ":", self.euler_func[n - 1])


class Improved_Euler():
    def improved_euler_method(self):
        print("Improved Euler")
        self.improved_euler_func = [0.0] * n
        self.improved_euler_func[0] = init.exact_func[0]
        i = 0
        while i < n - 1 and self.improved_euler_func[i] < sys.float_info.max:
            # and x[i] <= epsilon1
            print(i, ")", init.x[i], self.improved_euler_func[i])
            k1i = my_funct.f(init.x[i], self.improved_euler_func[i])
            k2i = my_funct.f(init.x[i] + init.h, self.improved_euler_func[i] + init.h * k1i)
            try:
                self.improved_euler_func[i + 1] = self.improved_euler_func[i] + init.h * (k1i + k2i) / 2
            except OverflowError:
                pass
            i += 1
        print("Improved Euler answer:", self.improved_euler_func[n - 1])


class Runge_Kutta():
    def runge_kutta_method(self):
        print("Runge-Kutta!")
        self.runge_kutta_func = [0.0] * n
        self.runge_kutta_func[0] = init.exact_func[0]
        i = 0
        while i < n - 1 and self.runge_kutta_func[i] < sys.float_info.max:
            # and x[i] <= epsilon1
            print(i, ")", init.x[i], self.runge_kutta_func[i])
            k1i = my_funct.f(init.x[i], self.runge_kutta_func[i])
            k2i = my_funct.f(init.x[i] + init.h / 2, self.runge_kutta_func[i] + init.h * k1i / 2)
            k3i = my_funct.f(init.x[i] + init.h / 2, self.runge_kutta_func[i] + init.h * k2i / 2)
            k4i = my_funct.f(init.x[i] + init.h, self.runge_kutta_func[i] + init.h * k3i)
            try:
                self.runge_kutta_func[i + 1] = self.runge_kutta_func[i] + init.h * (k1i + 2 * k2i + 2 * k3i + k4i) / 6
            except OverflowError:
                pass
            i += 1
        print("Runge-Kutta answer:", self.runge_kutta_func[n - 1])


class Exact():
    def exact_solution(self):
        self.exact_func = [0.0] * n
        self.exact_func[0] = init.exact_func[0]
        print("Exact\nc =", init.c)
        for i in range(n - 1):
            self.exact_func[i] = ((-3.0) * e ** (2.0 * init.x[i])) / (
                    init.c + e ** (3.0 * init.x[i]))
            print(i, init.x[i], self.exact_func[i])
        print("Exact solution at", init.x[n - 1], ":", self.exact_func[n - 1])


class Init:
    def init(self, x, y, X):
        self.x, self.exact_func, self.runge_kutta_func = [0.0] * n, [0.0] * n, [
            0.0] * n
        # x[0], y[0], X = 1.0, 0.5, 1.3
        # x[0], y[0], X = 1.6, -1.289138015374262, 7
        self.x[0], self.exact_func[0], self.X = x, y, X
        self.h = (self.X - self.x[0]) / n
        print("h (aka step) =", self.h)
        for i in range(n - 1):
            self.x[i + 1] = self.x[i] + self.h
        self.runge_kutta_func[0] = self.exact_func[0]
        self.c = e ** (2.0 * self.x[0]) * (-3.0) / self.exact_func[0] - e ** (
                3.0 * self.x[0])
        self.asymptote = (1 / 3) * (log(-self.c, e))
        print("vertical asymptote at x = ", self.asymptote)
        self.epsilon1 = self.asymptote - self.h / 2
        self.epsilon2 = self.asymptote + self.h / 2
        print("eps", self.epsilon1, self.epsilon2)
        self.last_y = self.exact_func[0]


n = 50
init = Init()
init.init(1.6, -1.289138015374262, 7)
my_funct = My_function()
exact = Exact()
euler = Euler()
improved = Improved_Euler()
runge_kutta = Runge_Kutta()
exact.exact_solution()
euler.euler_method()
improved.improved_euler_method()
runge_kutta.runge_kutta_method()

fig = plt.figure()
plt.plot(init.x, exact.exact_func, 'b', label='Exact')
plt.plot(init.x, euler.euler_func, 'g', label='Euler')
plt.plot(init.x, improved.improved_euler_func, 'c', label='Improved Euler')
plt.plot(init.x, runge_kutta.runge_kutta_func, 'm', label='Runge-Kutta')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Plots of the given function')
plt.legend()

plt.show()

# fig.savefig('test.jpg')
