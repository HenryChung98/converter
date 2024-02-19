from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

class BaseWindow:

    def __init__(self, title, geometry):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry(geometry)


class DBMRWindow(BaseWindow):
    def __init__(self):
        super().__init__("DBMR", "470x100+720+250")
        self.frame = Frame(self.window, width=450, height=80)
        self.frame.place(x=10, y=10)
        
        self.entry = Entry(self.frame, width=5)
        self.entry.place(x=10, y=20)
        self.label = Label(self.frame, text="kg")
        self.label.place(x=70, y=20)

        activity_level = [("Inactive"), ("Lightly Acitve"), ("Moderately Active"),
                          ("Heavily Active"), ("Exceptionaly Active")]
        self.select_activity = ttk.Combobox(self.frame, values=activity_level, width=11)
        self.select_activity.place(x=110, y=20)
        
        self.choice=StringVar()
        self.choice.set("MALE")
        self.rb1 = Radiobutton(self.frame, text="Male", font=14, variable=self.choice, value="MALE")
        self.rb1.place(x=250, y=10)
        self.rb1 = Radiobutton(self.frame, text="Female", font=14, variable=self.choice, value="FEMALE")
        self.rb1.place(x=250, y=30)
        
        self.button = Button(self.frame, text="Convert", font=14, command=self.do_this)
        self.button.place(x=350, y=20)
        
    def do_this(self):
        
        try:
            mass = float(self.entry.get())
            gender = self.choice.get()
            activity = self.select_activity.get()
            output_val1 = 0
            output_val2 = 0
            dbmr = mass * (24 if gender == "MALE" else 22)
            
        except:
            showerror("Error", "Please type valid value in entry box")
            
        else:
            if gender == "MALE":
                if activity == "Inactive":
                    output_val1 = dbmr + mass * 0.25
                    output_val2 = dbmr + mass * 0.40
                    showinfo("Result", f"{output_val1} to {output_val2}")
                
                elif activity == "Lightly Active":
                    output_val1 = dbmr + mass * 0.50
                    output_val2 = dbmr + mass * 0.70
                    showinfo("Result", f"{output_val1} to {output_val2}")
                    
                elif activity == "Moderately Active":
                    output_val1 = dbmr + mass * 0.65
                    output_val2 = dbmr + mass * 0.80
                    showinfo("Result", f"{output_val1} to {output_val2}")
                
                elif activity == "Heavily Active":
                    output_val1 = dbmr + mass * 0.90
                    output_val2 = dbmr + mass * 1.20
                    showinfo("Result", f"{output_val1} to {output_val2}")
                    
                elif activity == "Exceptionaly Active":
                    output_val1 = dbmr + mass * 1.30
                    output_val2 = dbmr + mass * 1.45
                    showinfo("Result", f"{output_val1} to {output_val2}")
                
            elif gender =="FEMALE":
                if activity == "Inactive":
                    output_val1 = dbmr + mass * 0.25
                    output_val2 = dbmr + mass * 0.35
                    showinfo("Result", f"{output_val1} to {output_val2}")
                
                elif activity == "Lightly Active":
                    output_val1 = dbmr + mass * 0.40
                    output_val2 = dbmr + mass * 0.60
                    showinfo("Result", f"{output_val1} to {output_val2}")
                    
                elif activity == "Moderately Active":
                    output_val1 = dbmr + mass * 0.50
                    output_val2 = dbmr + mass * 0.70
                    showinfo("Result", f"{output_val1} to {output_val2}")
                
                elif activity == "Heavily Active":
                    output_val1 = dbmr + mass * 0.80
                    output_val2 = dbmr + mass * 1.00
                    showinfo("Result", f"{output_val1} to {output_val2}")
                    
                elif activity == "Exceptionaly Active":
                    output_val1 = dbmr + mass * 1.10
                    output_val2 = dbmr + mass * 1.30
                    showinfo("Result", f"{output_val1} to {output_val2}")
                
            else:
                showerror("Error", "Please select your gender")