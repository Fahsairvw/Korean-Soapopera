import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot_graph import Storytelling, WhateverGraph, descriptive


class DisplayStory(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.init_component()
        self.graph = Storytelling()
        self.fig = None

    def init_component(self):
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label='GraphMenu', command=self.graph_menu)
        file_menu.add_command(label='StoryTelling')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)
        menu.add_cascade(label='Menu', menu=file_menu)
        self.config(menu=menu)

        """creating frame"""
        f = tk.Frame(self)
        f2 = tk.Frame(self)
        f3 = tk.Frame(self)
        f3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        f.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        f2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas_frame = tk.Canvas(f, bg='black', highlightthickness=0)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        """creating label"""
        label = tk.Label(f3, text='Story Telling', bg="#9bdeac", fg="#f7f5dd")
        label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        """creating button"""
        first = tk.Button(f2, text='1', command=self.first)
        first.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        second = tk.Button(f2, text='2', command=self.second)
        second.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        third = tk.Button(f2, text='3', command=self.third)
        third.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def display_graph(self):
        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.graph_canvas.draw()
        canvas_widget = self.graph_canvas.get_tk_widget()
        canvas_widget.grid(column=0, row=0, columnspan=3, sticky="news")
        self.fig = None

    def first(self):
        self.fig = self.graph.first_graph()
        self.display_graph()

    def second(self):
        self.fig = self.graph.second_graph()
        self.display_graph()

    def third(self):
        self.fig = self.graph.third_graph()
        self.display_graph()

    def graph_menu(self):
        self.destroy()
        ui = GraphMenu()
        ui.run()

    def run(self):
        self.mainloop()


class GraphMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.init_component()
        self.graph = WhateverGraph()
        self.fig = None
        self.attributes = None

    def init_component(self):
        """create menu"""
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label='GraphMenu')
        file_menu.add_command(label='StoryTelling', command=self.story_telling)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)
        menu.add_cascade(label='Menu', menu=file_menu)
        self.config(menu=menu)

        """create notebook for graph and descriptive"""
        notebook = ttk.Notebook(self)
        frame = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        notebook.pack(pady=10, expand=True)

        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        notebook.add(frame, text='Graph')
        notebook.add(frame2, text='Descriptive')

        """creating frame for graph"""
        f = tk.Frame(frame)
        f.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        f2 = tk.Frame(frame)
        f2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        """creating label"""
        t_button = tk.Label(f, text='Graph Type', highlightthickness=0)
        g_button = tk.Label(f, text='Graph Detail', highlightthickness=0)

        """creating button"""
        p_button = tk.Button(f, text='Plot', highlightthickness=0, command=self.display)
        exit_butt = tk.Button(f, text='Exit', command=self.destroy)

        """creating combobox"""
        self.t_combo = ttk.Combobox(f)
        self.t_combo['value'] = ['pie', 'histogram', 'scatter plot', 'heatmap']
        self.t_combo['state'] = 'readonly'
        self.t_combo.bind('<<ComboboxSelected>>', self.graph_type)
        self.g_combo = ttk.Combobox(f)
        self.g_combo['state'] = 'readonly'
        self.g_combo.bind('<<ComboboxSelected>>', self.graph_type)

        """create canvas"""
        self.canvas = tk.Canvas(f2, bg='black')

        """packing in frame"""
        t_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.t_combo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        g_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.g_combo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        p_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        exit_butt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        """Descriptive part"""
        num = ['No of Episode', 'Duration(minute)', 'Rating']
        info = descriptive()
        tree = ttk.Treeview(frame2)
        tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        tree['columns'] = num
        tree.column("#0", width=150, minwidth=150)
        tree.heading("#0", text="Statistic")

        for col in num:
            tree.column(col, width=100, minwidth=100, anchor=tk.E)
            tree.heading(col, text=col)

        for stat in info.index:
            stat_node_id = tree.insert("", tk.END, text=stat.capitalize())
            for col in num:
                value = info.loc[stat, col]
                tree.insert(stat_node_id, tk.END, text=f"{col}: {value:.2f}")

    def story_telling(self):
        self.destroy()
        ui = DisplayStory()
        ui.run()

    def display_graph(self, *args):
        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self.canvas)
        self.graph_canvas.draw()
        canvas_widget = self.graph_canvas.get_tk_widget()
        canvas_widget.grid(column=0, row=0, columnspan=3, sticky="news")
        self.attributes = None
        self.fig = None

    def graph_type(self, *args):
        graph = self.t_combo.get()

        if graph == 'pie':
            self.g_combo['value'] = ['rating']
            self.attribute = self.g_combo.get()
            self.selected_attribute_pie(self.attribute)
        if graph == 'histogram':
            self.g_combo['value'] = ['Year', 'No of Episode', 'Duration(minute)', 'Rating']
            self.attribute = self.g_combo.get()
            self.selected_attribute_histogram(self.attribute)
        if graph == 'scatter plot':
            self.g_combo['value'] = ['Rating & Duration(minute)']
            self.attribute = self.g_combo.get()
            self.selected_attribute_scatterplot(self.attribute)

        if graph == 'heatmap':
            self.g_combo['value'] = ['numerical data']
            self.attribute = self.g_combo.get()
            self.selected_attribute_heatmap(self.attribute)

    def selected_attribute_pie(self, attribute, *args):
        if attribute:
            self.fig = self.graph.pie()

    def selected_attribute_heatmap(self, attribute, *args):
        if attribute:
            self.fig = self.graph.heat_map()

    def selected_attribute_histogram(self, attribute, *args):
        if attribute:
            self.fig = self.graph.histogram(attribute)

    def selected_attribute_scatterplot(self, attribute, *args):
        if attribute:
            self.fig = self.graph.scatter_plot()

    def display(self, event=None):
        """call display function"""
        if self.fig is not None:
            self.display_graph(self.fig)

    def run(self):
        self.mainloop()



