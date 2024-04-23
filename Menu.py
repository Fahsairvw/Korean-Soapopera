import tkinter as tk


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.init_component()

    def init_component(self):
        pass


class Display(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Korean SoapOpera')
        self.init_component()
        self.geometry('900x500')

    def init_component(self):
        """Define background"""
        bg = tk.PhotoImage(file='output-onlinepngtools.png')
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.pack(fill='both', expand=True)

        background = tk.Label(canvas, image=bg)
        background.image = bg
        background.place(x=0, y=0, relwidth=1, relheight=1)

        """play back button"""
        play_back = tk.Button(canvas, text='⏮', command=self.previous_page)
        play_back.place(x=540, y=250)

        """next page button"""
        next_butt = tk.Button(canvas, text='⏭', command=self.next_page)
        next_butt.place(x=740, y=250)

    def next_page(self):
        pass

    def previous_page(self):
        pass

    def run(self):
        self.mainloop()


