# plVioletProject #

# AE Calculator (Almost Everything Calculator) #
 - - - -

A Calculator that includes common scientific/math formulas. A selection will appear to determine the formula to be used, then it will present the variables needed for the computation. Once the variables are presented, the user will input the values to be calculated then it will present the answer.

Some formulas to be included are:
Common Chemistry Formulas
Common Physics Formulas

The goal of this project is to make solving these common formulas easier using a python program.

Leader: John Dale Rick A. Nepomuceno

Rapporteur: Jeriah Robert N. Galang

Member: Allana A. Navajas

 - - - -

## :raising_hand: Click here for [Demonstration Video](https://youtu.be/ePceWaxhx9w "Demonstration") :point_left: via YouTube ##
## :open_book: Click here for [User Manual](https://github.com/yawna000/plVioletProject/blob/main/AE%20Calculator%20User%20Manual.pdf "User Manual") :point_left: ##

![picture alt](https://github.com/yawna000/plVioletProject/blob/main/Poster_AECalculator.png)

# IPO #

Input  | Process | Output
| :---: | :---:| :---: 
(1), (1), Mass (kg), Volume (m^3) | density = (mass / volume) | Density (kg/m^3)
(1), (2), Fahrenheit (F) | celsius = ((fahrenheit - 32) * 5/9) | Celsius (C)
(1), (3), Celsius (C) | fahrenheit = ((celsius * 9/5) + 32) | Fahrenheit (F)
(1), (4), Celsius (C) | kelvin = (celsius + 273.15) | Kelvin (K)
(1), (5), Kelvin (K) | celsius = (kelvin - 273.15) | Celsius (C)
(1), (6), Pressure 2 (Pa), Volume1 (m^3), Volume 2 (m^3) | pressure1 = (pressure2 * volume2) / volume1 | Pressure 1 (Pa)
(1), (7), Pressure 1 (Pa), Volume1 (m^3), Volume 2 (m^3) | pressure2 = (pressure1 * volume2) / volume1 | Pressure 2 (Pa)
(1), (8), Pressure 1 (Pa), Pressure 2 (Pa), Volume 2 (m^3) | volume1 = (pressure1 * volume2) / pressure2 | Volume 1 (m^3)
(1), (9), Pressure 1 (Pa), Pressure 2 (Pa), Volume 1 (m^3)| volume2 = (pressure2 * volume1) / pressure1 | Volume 2 (m^3)
(1), (10), Pressure 1 (Pa), Pressure 2 (Pa), Volume 2 (m^3), Temperature 1 (C) , Temperature 2 (C) | volume1 = ((pressure2 * volume2 * temperature1)/ (pressure1 * temperature2)) | Volume 1 (m^3)
(1), (11), Pressure 1 (Pa), Pressure 2 (Pa), Volume 1 (m^3), Temperature 1 (C) , Temperature 2 (C) | volume2 = ((pressure1 * volume1 * temperature2)/ (pressure2 * temperature1)) | Volume 2 (m^3)
(1), (12), Pressure 2 (Pa), Volume 1 (m^3), Volume 2 (m^3), Temperature 1 (C) , Temperature 2 (C) | pressure1 = ((pressure1 * volume1 * temperature1)/ (pressure2 * volume2)) | Pressure 1 (Pa)
(1), (13), Pressure 1 (Pa), Volume 1 (m^3), Volume 2 (m^3), Temperature 1 (C) , Temperature 2 (C) | pressure2 = ((pressure2 * volume2 * temperature1)/ (volume1 * temperature2)) | Pressure 2 (Pa)
(1), (14), Pressure 1 (Pa), Pressure 2 (Pa), Volume 1 (m^3), Volume 2 (m^3) , Temperature 2 (C) | temperature1 = ((pressure1 * volume1 * temperature2)/ (pressure2 * volume2)) | Temperature 1 (C)
(1), (15), Pressure 1 (Pa), Pressure 2 (Pa), Volume 1 (m^3), Volume 2 (m^3) , Temperature 1 (C) | temperature2 = ((pressure1 * volume1 * temperature1)/ (pressure2 * volume2)) | Temperature 2 (C)
(2), (1), Distance (m), Time (s) | speed = (distance/time) | Speed (m/s)
(2), (2), Displacement (m), Time (s) | velocity = (displacement/time) | Velocity (m/s)
(2), (3), Change in velocity (m/s), Time (s) | acceleration = (velocity/time) | Acceleration (m/s^2)
(2), (4), Distance (m), Time (s) | kinetic energy = (1/2 * mass * velocity^2) | Kinetic Energy (J)
(2), (5), Force (N), Distance (m) | work = (force * distance) | Work (Nm)
(2), (6), Force (N), Area (m^2) | pressure = (force/area) | Pressure (Pa)
(2), (7), Mass (kg), Area (m^2)  | force = (mass * area) | Force (N)
(2), (8), Mass (kg), Velocity (m/s) | momentum = (mass * velocity) | Momentum (kgm/s)
(2), (9), Work (Nm), Time (s) | power = (work/time) | Power (W)
(2), (10), Current (A), Resistance (ohm) | voltage = (current * resistance) | Voltage (V)
(2), (11), Voltage (V), Resistance (ohm) | current = (voltage / resistance) | Current (A)
(2), (12), Voltage (V), Current (A) | resistance = (voltage / current) | Resistance (ohm)
(2), (13), First charge (C), Second charge (C), Distance (m) | coulomb's law = (k * 1st charge * 2nd charge) / (d^2) | Force (N)
(2), (14), Current (A), Number of electrons, Area (m^2), Charge (C) | velocity = (current / (n * area * charge) ) | Force (N)
(3) | "Thank you for using AECalculator" | Terminate Program

