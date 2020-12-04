#Physics Formulas
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
