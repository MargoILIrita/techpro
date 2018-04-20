import matplotlib.pyplot as mtp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import legacycode

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea of BTC client")

        container = tk.Frame(self)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.f = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.get_tk_widget().grid(row=3, column=1, columnspan=4)
        toolbar_frame = tk.Frame()
        toolbar_frame.grid(row=4, column=1, columnspan=4)
        toolbar = NavigationToolbar2TkAgg(self.canvas, toolbar_frame)
        toolbar.update()
        def graph():
            try:
                n = int(nEntry.get())
                end = int(endEntry.get())
                func = type.get()
                self.f.clear()
                fig = self.f.add_subplot(111)
                if func[0] == "0":
                    x, y = legacycode.thirdfordraw(end, n)
                    leg1 = fig.plot(x, y, color="r")
                    fig.legend(leg1, "Метод Рунге-Кутта 3 порядка")
                if func[0] == "1":
                    x, y = legacycode.forthfordraw(end, n)
                    leg1 = fig.plot(x, y, color="b")
                    fig.legend(leg1, "Метод Рунге-Кутта 4 порядка")
                if func[0] == "2":
                    x, y = legacycode.thirdfordraw(end, n)
                    x1, y1 = legacycode.forthfordraw(end, n)
                    leg1, leg2 = fig.plot(x, y, x, y1)
                    fig.legend((leg1, leg2), ("Метод Рунге-Кутта 3 порядка", "Метод Рунге-Кутта 4 порядка"))
                fig.grid(True)
                self.canvas.show()
            except ValueError:
                tk.messagebox.showerror("Error", "Not valid argument")

        tk.Label(self, text = "N = ").grid(row=1, column=1)
        nEntry = tk.Entry(self, width=20)
        nEntry.grid(row=1,column=2)
        tk.Label(self, text="End = ").grid(row=2, column=1)
        endEntry = tk.Entry(self, width=20)
        endEntry.grid(row=2,column=2)
        type = tk.StringVar()
        type.set('0 Метод Рунге-Кутта 3 порядка')
        fspis=tk.OptionMenu(self, type,
                '0 Метод Рунге-Кутта 3 порядка',
                '1 Метод Рунге-Кутта 4 порядка',
                '2 Оба графика')
        fspis.grid(row=1,column=3)
        btn = ttk.Button(self, text="Graph", command=graph)
        btn.grid(row=1,column=4)

if __name__ == '__main__':
    app = App()
    app.mainloop()