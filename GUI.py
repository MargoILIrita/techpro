import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np
import pylab

import tkinter as tk
from tkinter import ttk
#import legacycode

LARGE_FONT = ("Verdana", 12)
global n
n = 0

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea of BTC client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        def graph():
            label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button1 = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(StartPage))
            button1.pack()
            x = np.arange(-10, 11, 1)
            y = x
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            global n
            print(n)
            a.plot(x, y)
            canvas = FigureCanvasTkAgg(f, self)
            canvas.show()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2TkAgg(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        def click_btn():
            global n
            n = nEntry.get()
            graph()

        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Start Page", font=LARGE_FONT).pack(pady=10, padx=10)
        nEntry = tk.Entry(self, width = 20)
        nEntry.pack()
        btn = ttk.Button(self, text="Graph", command = click_btn)
        tk.Radiobutton(self, text="GraphRK3", value = 1).pack()
        tk.Radiobutton(self, text="GraphRK4", value = 2).pack()
        tk.Radiobutton(self, text="GraphAll", value = 3).pack()
        btn.pack()


app = SeaofBTCapp()
app.mainloop()