import CalculatorFormulas
print('Welcome to AECalculator'
      '\n Please input 1 for Chemistry Formulas'
      '\n Please input 2 for Physics Formulas'
      '\n Please input 3 to end the program')
try:
    while True:
        x = int(input("What would you like to solve?: "))
        if x == 1:
            print('Choose your desired formula'
                  '\n Please input 1 for Density'
                  '\n Please input 2 for Fahrenheit to Celsius Conversion'
                  '\n Please input 3 for Celsius to Fahrenheit Conversion'
                  '\n Please input 4 for Celsius to Kelvin Conversion'
                  '\n Please input 5 for Kelvin to Celsius Conversion')
            y = int(input("Which formula would you like to solve?: "))
            if y == 1:
                print(float(CalculatorFormulas.density()))
            elif y == 2:
                print(float(CalculatorFormulas.fahrenheit_to_celsius()))
            elif y == 3:
                print(float(CalculatorFormulas.celsius_to_fahrenheit()))
            elif y == 4:
                print(float(CalculatorFormulas.celsius_to_kelvin()))
            elif y == 5:
                print((float(CalculatorFormulas.kelvin_to_celsius())))
            else:
                print("Enter a valid Command")
        elif x == 2:
            print('Choose your Desired Formula'
                  '\n Please input 1 for Speed'
                  '\n Please input 2 for Velocity'
                  '\n Please input 3 for Acceleration'
                  '\n Please input 4 for Kinetic Energy'
                  '\n Please input 5 for Work')
            y = int(input("Which formula would you like to solve?: "))
            if y == 1:
                print(float(CalculatorFormulas.speed()))
            elif y == 2:
                print(float(CalculatorFormulas.velocity()))
            elif y == 3:
                print(float(CalculatorFormulas.acc()))
            elif y == 4:
                print(float(CalculatorFormulas.ke()))
            elif y == 5:
                print(float(CalculatorFormulas.work()))
            else:
                print("Enter a valid Command")
        elif x == 3:
            print("Thank you for using AECalculator")
            exit()
        else:
            print("Enter a valid Command")
except ValueError:
    print("Enter a Valid Input")