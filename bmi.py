from tkinter import *
from tkinter.messagebox import *

class BaseWindow:

    def __init__(self, title, geometry):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry(geometry)


class BMIWindow(BaseWindow):
    def __init__(self):
        super().__init__("BMI", "270x350+720+50")
        self.frame = Frame(self.window, width=250, height=330)
        self.frame.place(x=10, y=10)
        
        self.numerator = Label(self.frame, text="Mass in kg", font=14)
        self.numerator.place(x=10, y=30)
        self.entry1 = Entry(self.frame, width=8)
        self.entry1.place(x=10, y=50)
        
        self.divider = Label(self.frame, text="-------------     =")
        self.divider.place(x=10, y=80)
        
        self.denominator = Label(self.frame, text="Height in m", font=14)
        self.denominator.place(x=10, y=120)
        self.entry2 = Entry(self.frame, width=8)
        self.entry2.place(x=10, y=100)
        
        self.square = Label(self.frame, text="^2")
        self.square.place(x=92, y=100)
        
        self.button = Button(self.frame, text="Get BMI", font=14, width=7, command=self.calculateBmi)
        self.button.place(x=140, y=77)
        
        
        # table
        self.header1 = Label(self.frame, text="BMI", font=14, width=8, fg="black", bg="#e8e8e8")
        self.header1.place(x=43, y=200)
        self.header2 = Label(self.frame, text="Status", font=14, width=9, fg="black", bg="#e8e8e8")
        self.header2.place(x=122, y=200)
        self.underweight = Label(self.frame, text="≤ 18.4", font=14, width=8, fg="black", bg="#fde189")
        self.underweight.place(x=43, y=223)
        self.underweight_sta = Label(self.frame, text="Underweight", font=14, width=9, fg="black", bg="#ffffff")
        self.underweight_sta.place(x=122, y=223)
        self.normal = Label(self.frame, text="18.5 - 24.9", font=14, width=8, fg="black", bg="#8cd47e")
        self.normal.place(x=43, y=246)
        self.normal_sta = Label(self.frame, text="Normal", font=14, width=9, fg="black", bg="#ffffff")
        self.normal_sta.place(x=122, y=246)
        self.overweight = Label(self.frame, text="25.0 - 39.9", font=14, width=8, fg="black", bg="#fab54c")
        self.overweight.place(x=43, y=269)
        self.overweight_sta = Label(self.frame, text="Overweight", font=14, width=9, fg="black", bg="#ffffff")
        self.overweight_sta.place(x=122, y=269)
        self.obese = Label(self.frame, text="≥ 40.0", font=14, width=8, fg="black", bg="#f66861")
        self.obese.place(x=43, y=292)
        self.obese_sta = Label(self.frame, text="Obese", font=14, width=9, fg="black", bg="#ffffff")
        self.obese_sta.place(x=122, y=292)


    def calculateBmi(self):
        try:
            numerator = self.entry1.get()
            denominator = self.entry2.get()
            mass = float(numerator)
            height = float(denominator)
        except:
            showerror("Error", "Please type valid value in entry box")
        else:
            bmi = round(mass / (height ** 2), 2)
            showinfo("Result", "BMI : " + str(bmi))