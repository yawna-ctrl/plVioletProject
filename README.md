# plVioletProject

AE Calculator (Almost Everything Calculator) 

GUI Calculator that includes common scientific/math formulas.
A selection box will appear to determine the formula to be used, then it will present the variables needed for the computation.
Once the variables are presented a user input of the values are to be done then it will present the answer.

Some formulas to be included are:
temperature conversion,
density,
bmi calculator,
molar mass of an element etc.

Common Physics, Chemistry, Statistics, Calculus formulas are also to be included in the selection box.

Leader: John Dale Rick A. Nepomuceno

Rapporteur: Jeriah Robert N. Galang

Member: Allana A. Navajas

### IPO ###

![alt text](https://github.com/yawna000/plVioletProject/blob/main/IPO.png)

:brain: **AE Calculator** :brain:

*01/12/2020*

```import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

ttk.Label(window, text="AECalculator",
          background='blue', foreground="white",
          font=("Times New Roman", 15)).grid(row=0, column=1)

ttk.Label(window, text="Select the Formula to be used :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=5, padx=10, pady=25)

n = tk.StringVar()
chem_formulas = ttk.Combobox(window, width=27, textvariable=n)

chem_formulas['values'] = ("Density",
                        "Fahrenheit to Celsius",
                        "Celsius to Kelvin",
                        "Kelvin to Celsius",
                        "Mass Per Cent",
                           )

chem_formulas.grid(column=1, row=5)
chem_formulas.current()

window.mainloop()
```
*Formulas*

```#Physics Formulas
def speed():
    d = int(input('Distance (m): '))
    t = int(input('Time (s): '))
    s = float(d/t)
    limit_s = round(s, 2)
    return limit_s

def velocity():
    d = int(input('Displacement (m): '))
    t = int(input('Time (s): '))
    v = float(d/t)
    limit_v = round(v, 2)
    return limit_v

def acc():
    v = int(input('Change in velocity (m/s): '))
    t = int(input('Time (s): '))
    a = float(v/t)
    limit_a = round(a, 2)
    return limit_a

def ke():
    m = int(input('Distance (m): '))
    v = int(input('Time (s): '))
    ke = float(1/2 * m * v **2)
    limit_ke = round(ke, 2)
    return limit_ke

def work():
    f = int(input('Force (N): '))
    d = int(input('Distance (m): '))
    w = float(f*d)
    limit_w = round(w, 2)
    return limit_w

#Chemistry Formulas
def density():
    m = int(input('Mass (M): '))
    v = int(input('Volume (V): '))
    d = float(m*v)
    limit_d = round(d, 2)
    return limit_d

def fahrenheit_to_celsius():
    fah = int(input('Fahrenheit (F): '))
    cel = (fah - 32) * 5/9
    limit_cel = round(cel, 2)
    return limit_cel

def celsius_to_fahrenheit():
    cel = int(input('Celsius (C): '))
    fah = (cel * 9/5) + 32
    limit_fah = round(fah, 2)
    return limit_fah

def celsius_to_kelvin():
    cel = int(input('Celsius (C): '))
    kel = cel + 273.15
    limit_kel = round(kel, 2)
    return limit_kel

def kelvin_to_celsius():
    kel = int(input('Kelvin (K): '))
    cel = kel - 273.15
    limit_cel = round(cel, 2)
    return limit_cel
```
