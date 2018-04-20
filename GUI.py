import matplotlib.pyplot as mtp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import legacycode

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea of BTC client")

        container = tk.Frame(self)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        def graph():
            try:
                n = int(nEntry.get())
                end = int(endEntry.get())
                f = type.get()
                if f[0] == "0":
                    x, y = legacycode.thirdfordraw(end, n)
                    leg1 = mtp.plot(x, y)
                    mtp.legend(leg1, "Метод Рунге-Кутта 3 порядка")
                if f[0] == "1":
                    x, y = legacycode.forthfordraw(end, n)
                    leg1 = mtp.plot(x, y)
                    mtp.legend(leg1, "Метод Рунге-Кутта 4 порядка")
                if f[0] == "2":
                    x, y = legacycode.thirdfordraw(end, n)
                    x1, y1 = legacycode.forthfordraw(end, n)
                    leg1, leg2 = mtp.plot(x, y, x, y1)
                    mtp.legend((leg1, leg2), ("Метод Рунге-Кутта 3 порядка", "Метод Рунге-Кутта 4 порядка"))
                mtp.grid()
                mtp.show()
            except ValueError:
                tk.messagebox.showerror("Error", "Not valid argument")

        tk.Label(self, text = "N = ").grid(row=1)
        nEntry = tk.Entry(self, width=20)
        nEntry.grid(row=1,column=1)
        tk.Label(self, text="End = ").grid(row=2)
        endEntry = tk.Entry(self, width=20)
        endEntry.grid(row=2,column=1)
        #
        type = tk.StringVar()
        type.set('0 Метод Рунге-Кутта 3 порядка')
        fspis=tk.OptionMenu(self, type,
                '0 Метод Рунге-Кутта 3 порядка',
                '1 Метод Рунге-Кутта 4 порядка',
                '2 Оба графика')
        fspis.grid(row=1,column=3)
        btn = ttk.Button(self, text="Graph", command=graph)
        btn.grid(row=1,column=4)

app = App()
app.mainloop()