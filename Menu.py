import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot_graph import Storytelling

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
        pass

    def init_component(self):
        """Define background"""
        self.bg = tk.PhotoImage(file='Story_telling_50 (1).png')
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

        """play back button"""
        play_back = tk.Button(canvas, text='⏮', command=self.previous_page)
        play_back.place(x=540, y=250)

        """next page button"""
        next_butt = tk.Button(canvas, text='⏭', command=self.next_page)
        next_butt.place(x=740, y=250)

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack()

    def next_page(self):
        pass

    def previous_page(self):
        pass

    def run(self):
        self.mainloop()


