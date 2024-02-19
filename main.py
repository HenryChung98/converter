from tkinter import *
from tkinter.messagebox import *
from bmi import BMIWindow
from metric_converter import MetricConverterWindow
from conversion_factor import ConversionFactorWindow
from dbmr import DBMRWindow

class BaseWindow:

    def __init__(self, title, geometry):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry(geometry)
        self.frame = Frame(self.window, width=500, height=800)
        self.frame.pack()

class MyGUI:

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry("200x200+100+50")
        self.create_buttons()
        mainloop()

    def create_buttons(self):
        buttons_info = [
            ("Metric Converter", self.metric_converter),
            ("Conversion Factor", self.conv_fac),
            ("BMI", self.bmi),
            ("DBMR", self.dbmr),
        ]

        for i, (text, command) in enumerate(buttons_info):
            button = Button(self.mainWindow, text=text, font=("Arial", 14), width=15, command=command)
            button.place(x=10, y=10 + i * 50)

    def metric_converter(self):
        MetricConverterWindow()

    def conv_fac(self):
        ConversionFactorWindow()

    def bmi(self):
        BMIWindow()

    def dbmr(self):
        DBMRWindow()



my_gui = MyGUI()
