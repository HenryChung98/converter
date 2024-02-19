from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from pint import UnitRegistry

class BaseWindow:

    def __init__(self, title, geometry):
        self.window = Toplevel()
        self.window.title(title)
        self.window.geometry(geometry)


class ConversionFactorWindow(BaseWindow):
    def __init__(self):
        super().__init__("Conversion Factor", "340x170+720+250")
        self.frame = Frame(self.window, width=320, height=150)
        self.frame.place(x=10, y=10)
        self.entry = Entry(self.frame, width=7)
        self.entry.place(x=10, y=50)
        
        symbol_info = [("tsp"), ("tbsp"), ("cup"), ("mL"), ("L"), ("fluid oz"), ("cm"), ("lb"),
                       ("inch"), ("ft"), ("oz"), ("g"), ("kg"), ("°C"), ("°F"), ("J"),
                       ("calorie")]
        self.convert_from = ttk.Combobox(self.frame, values=symbol_info, width=5)
        self.convert_from.place(x=90, y=50)
        self.convert_to = ttk.Combobox(self.frame, values=symbol_info, width=5)
        self.convert_to.place(x=240, y=50)
        
        self.label = Label(self.frame, text="convert to", font=14)
        self.label.place(x=170, y=50)
        
        self.convertBtn = Button(self.frame, text="Convert", font=14, command=self.do_this)
        self.convertBtn.place(x=120, y=110)
        
    def do_this(self):
        ureg = UnitRegistry()
        Q_ = ureg.Quantity
        
        CONVERSION_FACTORS = {
            "tsp": ureg.teaspoon,
            "tbsp": ureg.tablespoon,
            "cup": ureg.cup,
            "mL": ureg.milliliter,
            "mL": ureg.liter,
            "fluid oz": ureg.fluid_ounce,
            "cm": ureg.centimeter,
            "lb": ureg.pound,
            "inch": ureg.inch,
            "ft": ureg.foot,
            "oz": ureg.ounce,
            "g": ureg.gram,
            "kg": ureg.kilogram,
            "°C": ureg.celsius,
            "°F": ureg.fahrenheit,
            "J": ureg.joule,
            "calorie": ureg.calorie,
            }
        
        try:
            input_val = float(self.entry.get())
            from_unit = self.convert_from.get()
            to_unit = self.convert_to.get()
            
        except:
            showerror("Error", "Please type valid value in entry box")
        
        else:
            try:
                input_quantity = Q_(input_val, from_unit)
                output_quantity = round(input_quantity.to(to_unit), 1)
                showinfo("Result", f"{output_quantity.magnitude} {to_unit}")
            except:
                showerror("Error", f"Conversion from {from_unit} to {to_unit} not supported")
            
