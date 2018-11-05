import os
import sys
from tkinter.ttk import Entry, Button

import numpy as np
from math import e, log
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib
import urllib
import json
import pandas as pd

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

# f = Figure(figsize=(5, 4), dpi=100)
f = plt.figure()
a = f.add_subplot(111)


def animate(i):
    pullData = open('sampleText.txt', 'r').read()
    dataArray = pullData.split('\n')
    xar = []
    exact_func_ar = []
    for eachLine in dataArray:
        x, y = eachLine.split(',')
        xar.append(float(x))
        exact_func_ar.append(float(y))
    a.clear()
    euler_animate()
    a.plot(xar, exact_func_ar, 'b')
    a.set_title("Plots of the function")
    a.set_xlabel('x')
    a.set_ylabel('y')
    f.legend(['Runge-Kutta', 'Improved Euler', 'Euler', 'Exact'])
    f.tight_layout()


def euler_animate():
    pullData = open('EulerText.txt', 'r').read()
    dataArray = pullData.split('\n')
    xar = []
    euler_func_ar = []
    for eachLine in dataArray:
        x, y = eachLine.split(',')
        xar.append(float(x))
        euler_func_ar.append(float(y))
    improved_euler_animate()
    a.plot(xar, euler_func_ar, 'g')


def improved_euler_animate():
    pullData = open('ImprovedEulerText.txt', 'r').read()
    dataArray = pullData.split('\n')
    xar = []
    improved_euler_func_ar = []
    for eachLine in dataArray:
        x, y = eachLine.split(',')
        xar.append(float(x))
        improved_euler_func_ar.append(float(y))
    runge_kutta_animate()
    a.plot(xar, improved_euler_func_ar, 'c')


def runge_kutta_animate():
    pullData = open('RungeKuttaText.txt', 'r').read()
    dataArray = pullData.split('\n')
    xar = []
    runge_kutta_func_ar = []
    for eachLine in dataArray:
        x, y = eachLine.split(',')
        xar.append(float(x))
        runge_kutta_func_ar.append(float(y))
    a.plot(xar, runge_kutta_func_ar, 'm')


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "DE assignment")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, BTCe_Page):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Error graph page",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()
        button2 = ttk.Button(self, text="Graph Page",
                             command=lambda: controller.show_frame(BTCe_Page))
        button2.pack()
        e1 = Entry()
        e1.pack()
        e1.focus_set()

        def callback():
            the_file = open("input.txt", 'w')
            the_file.write(e1.get())
            the_file.close()

            print(e1.get())

        b = Button(text='Enter n and press the button', command=callback)
        b.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class BTCe_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()

import os
import sys
import numpy as np
from math import e, log
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib


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


my_file = open("input.txt", "r")
n = int(my_file.read())
# n = 25
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
my_file = open("sampleText.txt", "w")
i = 0
for i in range(n - 1):
    string = str(init.x[i]) + ", " + str(exact.exact_func[i])
    my_file.write(string + "\n")
my_file.write(str(init.x[n - 1]) + ", " + str(exact.exact_func[n - 1]))
my_file.close()
my_file = open("EulerText.txt", "w")
i = 0
for i in range(n - 1):
    string = str(init.x[i]) + ", " + str(euler.euler_func[i])
    my_file.write(string + "\n")
my_file.write(str(init.x[n - 1]) + ", " + str(euler.euler_func[n - 1]))
my_file.close()

my_file = open("ImprovedEulerText.txt", "w")
i = 0
for i in range(n - 1):
    string = str(init.x[i]) + ", " + str(improved.improved_euler_func[i])
    my_file.write(string + "\n")
my_file.write(str(init.x[n - 1]) + ", " + str(improved.improved_euler_func[n - 1]))
my_file.close()

my_file = open("RungeKuttaText.txt", "w")
i = 0
for i in range(n - 1):
    string = str(init.x[i]) + ", " + str(runge_kutta.runge_kutta_func[i])
    my_file.write(string + "\n")
my_file.write(str(init.x[n - 1]) + ", " + str(runge_kutta.runge_kutta_func[n - 1]))
my_file.close()

# todo

ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
