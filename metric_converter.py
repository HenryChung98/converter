from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

class BaseWindow:

    def __init__(self, title, geometry):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry(geometry)


class MetricConverterWindow(BaseWindow):
    def __init__(self):
        super().__init__("Metric Converter", "340x500+720+50")
        self.frame = Frame(self.window, width=320, height=480)
        self.frame.place(x=10, y=10)
        
        self.header1 = Label(self.frame, text="Text", font=14)
        self.header1.place(x=10, y=0)
        self.header2 = Label(self.frame, text="Symbol", font=14)
        self.header2.place(x=80, y=0)
        self.header3 = Label(self.frame, text="Factor", font=14)
        self.header3.place(x=170, y=0)
        
        text_info = [("tera"), ("giga"), ("mega"), ("kilo"), ("hecto"), ("deca"),
                     ("deci"), ("centi"), ("milli"), ("micro"), ("nano"), ("pico")]

        for i, (text) in enumerate(text_info):
            label = Label(self.frame, text=text, font=14)
            if i >= 6:
                label.place(x=10, y=80 + i * 25)
            else:
                label.place(x=10, y=35 + i * 25)
            setattr(self, f"label{i+1}", label)
            
        symbol_info = [("T"), ("G"), ("M"), ("k"), ("h"), ("da"),
                       ("d"), ("c"), ("m"), ("µ"), ("n"), ("p")]
        
        for i, (symbol) in enumerate(symbol_info):
            label = Label(self.frame, text=symbol, font=14)
            if i >= 6:
                label.place(x=80, y=80 + i * 25)
            else:
                label.place(x=80, y=35 + i * 25)
            setattr(self, f"label{i+1}", label)
            
            
        factor_info = [("1 000 000 000 000"), ("1 000 000 000"), ("1 000 000"), ("1 000"), ("100"),
                       ("10"), ("0.1"), ("0.01"), ("0.001"), ("0.000 001"), ("0.000 000 001"),
                       ("0.000 000 000 001")]
        
        for i, (factor) in enumerate(factor_info):
            label = Label(self.frame, text=factor, font=14)
            if i >= 6:
                label.place(x=170, y=80 + i * 25)
            else:
                label.place(x=170, y=35 + i * 25)
            setattr(self, f"label{i+1}", label)
        
        
        self.entry = Entry(self.frame, width=8)
        self.entry.place(x=10, y=195)
        self.convertTo = Label(self.frame, text="Convert to", font=14)
        self.convertTo.place(x=100, y=195)
        self.factor_values = ttk.Combobox(self.frame, values=symbol_info, width=3)
        self.factor_values.place(x=180, y=193)
        self.convertBtn = Button(self.frame, text="Convert", font=("Arial", 14), width=7, command=self.do_this)
        self.convertBtn.place(x=110, y=420)
        

     
    def do_this(self):
        FACTOR_MULTIPLIERS = {"T": 1e12, "G": 1e9, "M": 1e6, "k": 1000, "h": 100, "da": 10,
                              "d": 0.1, "c": 0.01, "m":0.001, "µ": 1e-6, "n": 1e-9,
                              "p": 1e-12}
        try:
            input_val = float(self.entry.get())
            factor_val = self.factor_values.get()
            output_val = 0

        except:
            showerror("Error", "Please type valid value in entry box")
            
        else:
            if factor_val in FACTOR_MULTIPLIERS:
                output_val = input_val * FACTOR_MULTIPLIERS[factor_val]
                showinfo("Result", str(output_val) + factor_val)
            else:
                showerror("Error", "Please select the factor")
            
        