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
                  '\n Please input 5 for Kelvin to Celsius Conversion'
                  '\n Please input 6 for Boyles Law (P1)'
                  '\n Please input 7 for Boyles Law (P2)'
                  '\n Please input 8 for Boyles Law (V1)'
                  '\n Please input 9 for Boyles Law (V2)')
            y = int(input("Which formula would you like to solve?: "))
            if y == 1:
                print("Density is: ", float(CalculatorFormulas.density()))
            elif y == 2:
                print("Celsius is: ", float(CalculatorFormulas.fahrenheit_to_celsius()))
            elif y == 3:
                print("Fahrenheit is: ", float(CalculatorFormulas.celsius_to_fahrenheit()))
            elif y == 4:
                print("Kelvin is: ", float(CalculatorFormulas.celsius_to_kelvin()))
            elif y == 5:
                print("Celsius is: ", float(CalculatorFormulas.kelvin_to_celsius()))
            elif y == 6:
                print("P1 is: ", float(CalculatorFormulas.boyleP1()))
            elif y == 7:
                print("P2 is: ", float(CalculatorFormulas.boyleP2()))
            elif y == 8:
                print("V1 is: ", float(CalculatorFormulas.boyleV1()))
            elif y == 9:
                print("V2 is: ", float(CalculatorFormulas.boyleV2()))
            else:
                print("Enter a valid Command")
        elif x == 2:
            print('Choose your Desired Formula'
                  '\n Please input 1 for Speed'
                  '\n Please input 2 for Velocity'
                  '\n Please input 3 for Acceleration'
                  '\n Please input 4 for Kinetic Energy'
                  '\n Please input 5 for Work'
                  '\n Please input 6 for Pressure'
                  '\n Please input 7 for Force'
                  '\n Please input 8 for Momentum'
                  '\n Please input 9 for Power'
                  '\n Please input 10 for Volt'
                  '\n Please input 11 for Current'
                  '\n Please input 12 for Resistance'
                  '\n Please input 13 for Coulombs Law'
                  '\n Please input 14 for Drift Velocity')
            y = int(input("Which formula would you like to solve?: "))
            if y == 1:
                print("Speed is: ", float(CalculatorFormulas.speed()))
            elif y == 2:
                print("Velocity is: ", float(CalculatorFormulas.velocity()))
            elif y == 3:
                print("Acceleration is: ", float(CalculatorFormulas.acc()))
            elif y == 4:
                print("Kinetic Energy is: ", float(CalculatorFormulas.ke()))
            elif y == 5:
                print("Work is: ", float(CalculatorFormulas.work()))
            elif y == 6:
                print("Pressure is: ", float(CalculatorFormulas.pressure()))
            elif y == 7:
                print("Force is: ", float(CalculatorFormulas.force()))
            elif y == 8:
                print("Momentum is: ", float(CalculatorFormulas.momen()))
            elif y == 9:
                print("Power is: ", float(CalculatorFormulas.power()))
            elif y == 10:
                print("Volt is: ", float(CalculatorFormulas.volt()))
            elif y == 11:
                print("Current is: ", float(CalculatorFormulas.current()))
            elif y == 12:
                print("Resistance is: ", float(CalculatorFormulas.resistance()))
            elif y == 13:
                print("Coulomb is: ", float(CalculatorFormulas.coulombslaw()))
            elif y == 14:
                print("Drift Velocity is: ", float(CalculatorFormulas.driftv()))
            else:
                print("Enter a valid Command")
        elif x == 3:
            print("Thank you for using AECalculator")
            exit()
        else:
            print("Enter a valid Command")
except ValueError:
    print("Enter a Valid Input")