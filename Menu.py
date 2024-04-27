import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot_graph import Storytelling, WhateverGraph


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.init_component()

    def storytelling_menu(self, event):
        self.destroy()
        ui = DisplayStory()
        ui.run()

    def graph_menu(self, event):
        self.destroy()
        ui = GraphMenu()
        ui.run()

    def init_component(self):
        """Define background"""
        self.bg = tk.PhotoImage(file='menu_pic.png')
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.pack(fill='both', expand=True)

        background = tk.Label(canvas, image=self.bg)
        background.image = self.bg
        background.place(x=0, y=0, relwidth=1, relheight=1)

        """Define Story telling Menu Button"""
        first_menu = tk.Button(self, text='Story Telling menu')
        first_menu.bind('<Button>', self.storytelling_menu)
        first_menu.place(x=360, y=300)
        """Define Graph Menu Button"""
        second_menu = tk.Button(self, text='Graph menu')
        second_menu.bind('<Button>', self.graph_menu)
        second_menu.place(x=380, y=350)

    def run(self):
        self.mainloop()


class DisplayStory(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.init_component()
        self.geometry('890x490')
        self.page = 1
        self.graph = Storytelling()

    def init_component(self):
        """Define background"""
        self.bg = tk.PhotoImage(file='output-onlinepngtools.png')
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.pack(fill='both', expand=True)

        background = tk.Label(canvas, image=self.bg)
        background.image = self.bg
        background.place(x=0, y=0, relwidth=1, relheight=1)

        """first graph button"""
        first_butt = tk.Button(canvas, text='first', command=self.first_page)
        first_butt.place(x=540, y=250)

        """second graph button"""
        second_butt = tk.Button(canvas, text='second', command=self.second_page)
        second_butt.place(x=725, y=250)

        """third graph button"""
        third_butt = tk.Button(canvas, text='third', command=self.third_page)
        third_butt.place(x=625, y=340)

        self.canvas_frame = tk.Canvas(canvas, width=350, height=250, bg='black', highlightthickness=0)
        self.text_id = self.canvas_frame.create_text(175, 100, text="Story Telling", fill="#9bdeac",
                                      font=("Courier", 35, 'bold'))
        self.canvas_frame.place(x=100, y=120)

    def first_page(self):
        self.canvas_frame.itemconfig(self.text_id, text='First graph', fill="#9bdeac",
                                     font=("Courier", 35, 'bold'))
        self.graph.first_graph()
        self.canvas_frame.itemconfig(self.text_id, text='Story Telling', fill="#9bdeac",
                                     font=("Courier", 35, 'bold'))

    def second_page(self):
        self.canvas_frame.itemconfig(self.text_id, text='Second graph', fill="#9bdeac",
                                     font=("Courier", 35, 'bold'))
        self.graph.second_graph()
        self.canvas_frame.itemconfig(self.text_id, text='Story Telling', fill="#9bdeac",
                                     font=("Courier", 35, 'bold'))

    def third_page(self):
        self.canvas_frame.itemconfig(self.text_id, text='Third graph', fill="#9bdeac",
                                     font=("Courier", 35, 'bold'))
        self.graph.third_graph()
        self.canvas_frame.itemconfig(self.text_id, text='Story Telling', fill="#9bdeac",
                                     font=("Courier", 35, 'bold'))

    def run(self):
        self.mainloop()


class GraphMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.config(bg='black')
        self.init_component()
        self.numerical = ['No of Episode', 'Rating', 'Duration(minute)']
        self.graph_type = ['pie graph', 'heat map', 'scatter plot']
        self.graph = WhateverGraph()

    def init_component(self):
        f = tk.Frame(self)
        f.grid(row=0, column=0, columnspan=5, rowspan=2, sticky="nsew")
        f2 = tk.Frame(self)
        f2.grid(row=3, column=0, columnspan=5, rowspan=2, sticky="nsew")
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
        """create canvas"""
        fig = self.graph.pie()
        self.canvas = FigureCanvasTkAgg(fig, master=f2)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(column=0, row=0, columnspan=3, sticky="news")


    def run(self):
        self.mainloop()


