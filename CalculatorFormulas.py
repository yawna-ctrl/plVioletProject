#Physics Formulas
def speed():
    d = int(input('Distance : '))
    t = int(input('Time : '))
    s = float(d/t)
    limit_s = round(s, 2)
    return limit_s

def velocity():
    d = int(input('Displacement : '))
    t = int(input('Time : '))
    v = float(d/t)
    limit_v = round(v, 2)
    return limit_v

def acc():
    v = int(input('Change in velocity : '))
    t = int(input('Time : '))
    a = float(v/t)
    limit_a = round(a, 2)
    return limit_a

def pressure():
    f = int(input('Force : '))
    a = int(input('Area : '))
    p = float(f/a)
    limit_p = round(p, 2)
    return limit_p

def force():
    m = int(input('Mass : '))
    a = int(input('Area : '))
    f = float(m*a)
    limit_f = round(f, 2)
    return limit_f

def momen():
    m = int(input('Mass : '))
    v = int(input('Velocity : '))
    mo = float(m*v)
    limit_mo = round(mo, 2)
    return limit_mo

def power():
    w = int(input('Work : '))
    t = int(input('Time : '))
    p = float(w/t)
    limit_p = round(p, 2)
    return limit_p

def volt():
    i = int(input('Current : '))
    r = int(input('Resistance : '))
    voltage = float(i*r)
    limit_voltage = round(voltage, 2)
    return limit_voltage

def current():
    v = int(input('Voltage : '))
    r = int(input('Resistance : '))
    i = float(v/r)
    limit_i = round(i, 2)
    return limit_i

def resistance():
    v = int(input('Voltage : '))
    i = int(input('Current : '))
    r = float(v/i)
    limit_r = round(r, 2)
    return limit_r

def ke():
    m = int(input('Mass : '))
    v = int(input('Time : '))
    ke = float(1/2 * m * v **2)
    limit_ke = round(ke, 2)
    return limit_ke

def work():
    f = int(input('Force : '))
    d = int(input('Distance : '))
    w = float(f*d)
    limit_w = round(w, 2)
    return limit_w

def coulombslaw():
    k = 9000000000
    q1 = int(input('First charge : '))
    q2 = int(input('Second charge : '))
    d = int(input('Distance : '))
    f = float(k*q1*q2)/(d**2)
    limit_f = round(f, 2)
    return limit_f

def driftv():
    i = int(input('Current : '))
    n = int(input('Number of electrons: '))
    a = int(input('Area (m^2): '))
    q = int(input('Charge (C): '))
    v = float(i/n*a*q)
    limit_v = round(v, 2)
    return limit_v

#Chemistry Formulas
def density():
    m = int(input('Mass : '))
    v = int(input('Volume : '))
    d = float(m*v)
    limit_d = round(d, 2)
    return limit_d

def boyleP1 ():
    v1 = int(input('V1: '))
    v2 = int(input('V2: '))
    p2 = int(input('P2: '))
    p1 = (p2 * v2) / v1
    limit_p1 = round(p1, 2)
    return limit_p1

def boyleV1():
    p1 = int(input('P1: '))
    p2 = int(input('P2: '))
    v2 = int(input('V2: '))
    v1 = (p2 * v2) / p1
    limit_v1 = round(v1, 2)
    return limit_v1

def boyleP2():
    v1 = int(input('V1: '))
    v2 = int(input('V2: '))
    p1 = int(input('P1: '))
    p2 = (p1 * v2) / v1
    limit_p2 = round(p2, 2)
    return limit_p2

def boyleV2():
    p1 = int(input('P1: '))
    p2 = int(input('P2: '))
    v1 = int(input('V1: '))
    v2 = (p2 * v1) / p1
    limit_v2 = round(v2, 2)
    return limit_v2

def combined_gas_lawV1():
    p1 = int(input('P1: '))
    p2 = int(input('P2: '))
    v2 = int(input('V2: '))
    t1 = int(input('T1: '))
    t2 = int(input('T2: '))
    v1 = ((t1*p2*v2)/(p1*t2))
    limit_v1 = round(v1, 2)
    return limit_v1

def combined_gas_lawV2():
    p1 = int(input('P1: '))
    p2 = int(input('P2: '))
    v1 = int(input('V1: '))
    t1 = int(input('T1: '))
    t2 = int(input('T2: '))
    v2 = ((p1 * v1 * t2) / (t1 * p2))
    limit_v2 = round(v2, 2)
    return limit_v2

def combined_gas_lawP1():
    v2 = int(input('V2: '))
    p2 = int(input('P2: '))
    v1 = int(input('V1: '))
    t1 = int(input('T1: '))
    t2 = int(input('T2: '))
    p1 = ((t1 * p2 * v2) / (v1 * t2))
    limit_p1 = round(p1, 2)
    return limit_p1

def combined_gas_lawP2():
    p1 = int(input('P1: '))
    v1 = int(input('V1: '))
    t2 = int(input('T2: '))
    v2 = int(input('V2: '))
    t1 = int(input('T1: '))
    p2 = ((p1 * v1 * t2)/ (v2 * t1))
    limit_p2 = round(p2, 2)
    return limit_p2

def combined_gas_lawT1():
    p1 = int(input('P1: '))
    v1 = int(input('V1: '))
    t2 = int(input('T2: '))
    p2 = int(input('P2: '))
    v2 = int(input('V2: '))
    t1 = ((p1 * v1 * t2)/ (p2* v2))
    limit_t1 = round(t1, 2)
    return limit_t1

def combined_gas_lawT2():
    p1 = int(input('P1: '))
    v1 = int(input('V1: '))
    t1 = int(input('T2: '))
    p2 = int(input('P2: '))
    v2 = int(input('V2: '))
    t2 = ((p1 * v1 * t1)/ (p2* v2))
    limit_t2 = round(t2, 2)
    return limit_t2

def fahrenheit_to_celsius():
    fah = int(input('Fahrenheit : '))
    cel = (fah - 32) * 5/9
    limit_cel = round(cel, 2)
    return limit_cel

def celsius_to_fahrenheit():
    cel = int(input('Celsius : '))
    fah = (cel * 9/5) + 32
    limit_fah = round(fah, 2)
    return limit_fah

def celsius_to_kelvin():
    cel = int(input('Celsius : '))
    kel = cel + 273.15
    limit_kel = round(kel, 2)
    return limit_kel

def kelvin_to_celsius():
    kel = int(input('Kelvin : '))
    cel = kel - 273.15
    limit_cel = round(cel, 2)
    return limit_cel
