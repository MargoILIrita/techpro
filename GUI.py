import matplotlib.pyplot as mtp
import numpy as np
import pylab

import tkinter as tk
from tkinter import ttk
import legacycode

LARGE_FONT = ("Verdana", 12)
global n
n = 0
global x
global y
x = 0
y = 0

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea of BTC client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        def graph():
            n = int(nEntry.get())
            if n != 0:
                print(n)
            fn = type.get()
            f = fn[0]
            if f == "0":
                x,y = legacycode.thirdfordraw(n,n)
                leg1 = mtp.plot(x, y)
                mtp.legend(leg1,"Метод Рунге-Кутта 3 порядка")
                mtp.grid()
                mtp.show()

            if f == "1":
                x, y = legacycode.forthfordraw(n, n)
                leg1 = mtp.plot(x, y)
                mtp.legend(leg1,"Метод Рунге-Кутта 4 порядка")
                mtp.grid()
                mtp.show()
            if f == "2":
                x, y = legacycode.thirdfordraw(n, n)
                x1, y1 = legacycode.forthfordraw(n, n)
                leg1,leg2 = mtp.plot(x, y, x, y1)
                mtp.legend((leg1,leg2),("Метод Рунге-Кутта 3 порядка","Метод Рунге-Кутта 4 порядка"))
                mtp.grid()
                mtp.show()


        nEntry = tk.Entry(self, width=20)
        nEntry.pack(side=tk.LEFT)
        #
        type = tk.StringVar()
        type.set('0 Метод Рунге-Кутта 3 порядка')
        fspis=tk.OptionMenu(self, type,
                '0 Метод Рунге-Кутта 3 порядка',
                '1 Метод Рунге-Кутта 4 порядка',
                '2 Оба графика')
        fspis.pack({"side": "left"})
        btn = ttk.Button(self, text="Graph", command=graph)
        btn.pack(side=tk.LEFT)


app = App()
app.mainloop()