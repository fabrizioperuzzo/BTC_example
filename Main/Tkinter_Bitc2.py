import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


LARGE_FONT = ("Verdana", 12)

class SeaofBTapp(tk.Tk): # is an inheritance not a parameter Tk class within tkinter

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) #usually we do root=tk.Tk


        img_path = "image/clienticon.ico"
        photo = tk.PhotoImage(file=img_path)
        self.tk.call("wm", "iconphoto", self._w, photo)

        self.title("Sea Of BTC client")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {} # insieme di tutti i frame

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame = self.frames[cont] # cont is the key the value is grabbed in the dict
        frame.tkraise() #always on top  we can use the method .tkraise becuase we inherited tk.Tk

class StartPage(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):

        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="start page", font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page One", command= lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Visiti Page Two", command= lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)   # questo non ho capito perché devo farlo
        label = ttk.Label(self, text="Page One", font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Start Page", command= lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Visiti Page Two", command= lambda: controller.show_frame(PageTwo))
        button2.pack()



class PageTwo(tk.Frame):  # sono obbligato a fare una classe perchè deve ereditare tk.Frame

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)   # questo non ho capito perché devo farlo
        label = ttk.Label(self, text="Page Two", font= LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Start Page", command= lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Visiti Page One", command= lambda: controller.show_frame(PageOne))
        button2.pack()

app = SeaofBTapp() # it's like to do app= tk.TK()
app.mainloop()









