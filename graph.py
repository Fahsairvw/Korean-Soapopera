import tkinter as tk
from tkinter import ttk


class GraphMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.config(bg='black')
        self.init_component()
        self.columnconfigure(0, weight=1)

    def init_component(self):
        f = tk.Frame(self, bg='black')
        f.grid(row=0, column=0, columnspan=5, rowspan=2, sticky="EW")
        """create button"""
        t_button = tk.Button(f, text='graph type', highlightthickness=0)
        t_button.grid(row=1, column=0, sticky='NSEW')
        g_button = tk.Button(f, text='graphtype', highlightthickness=0)
        g_button.grid(row=1, column=2, sticky='NSEW')
        p_button = tk.Button(f, text='plot', highlightthickness=0)
        p_button.grid(row=1, column=4, sticky='NSEW')

        """create combobox"""
        t_combo = ttk.Combobox(f)
        t_combo.grid(row=1, column=1, sticky='NSEW')
        g_combo = ttk.Combobox(f)
        g_combo.grid(row=1, column=3, sticky='NSEW')

        for i in range(5):
            self.rowconfigure(i, weight=1)
        self.rowconfigure(1, weight=1)

    def run(self):
        self.mainloop()
