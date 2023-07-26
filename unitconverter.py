import time

def main_menu():
    while True:
        '''Main menu with choices of different converters.'''
        print("\n What would you like to do? Here are your converters:")
        print("\n '1' to convert temperatures in Celsius (C), Fahrenheit (F) and Kelvin(K).")
        print("\n '2' to convert masses in pounds (lb) and kilograms (kg).")
        print("\n '3' to convert lengths in meters (m) and feet (ft).")
        cmd = input("\n Enter your choice: ")
        if cmd == '1':
            tempconvert()
        elif cmd == '2':
            massconvert()
        elif cmd == '3':
            lengthconvert()
        else:
            print('\n', "'", cmd, "'", "is not an option. \n")
            time.sleep(1)

def afterConvert(again, choose,  unit, measure):
    '''Choices of things to do after getting a conversion: Do it again, choose another unit or go to main menu.'''
    time.sleep(3)
    print("\n '1' for another", unit, "conversion")
    print("\n '2' for another", measure, "unit conversion")
    print("\n '3' for the main menu")
    cmd = input("\n Select your next course of action: ")
    if cmd == '1':
        again()
    elif cmd == '2':
        choose()
    elif cmd == '3':
        main_menu()
    else:
        print('\n', "'", cmd, "'", "is not an option. \n")
        afterConvert(again, choose, unit, measure)

def lengthconvert():
    '''/choice of input length unit.'''
    while True:
        print("Length Converter \n 'm' for meters \n 'f' for feet")
        cmd = input("\n Enter the letter corresponding to your length: ")
        if cmd == 'm':
            converting_meter()
        elif cmd == 'f':
            converting_foot()
        else:
            print('\n', "'", cmd, "'", "is not an option. \n")
            time.sleep(1)

def converting_meter():
    '''Operations to convert meters to feet and print result.'''
    while True:
        try:
            M = float(input("\n Enter your length: "))
            F = round(M / 0.3048, 3)
            print("\n %s m is %s ft" % (M, F))
            afterConvert(converting_meter, lengthconvert, 'meter', 'length')
        except ValueError:
            print("\n That is not a number. Please try again.")

def converting_foot():
    '''Operations to convert feet to meters and print result.'''
    while True:
        try:
            F = float(input("\n Enter your length: "))
            M = round(F * 0.3048, 3)
            print("\n %s ft is %s m" % (F, M))
            afterConvert(converting_foot, lengthconvert, 'foot', 'length')
        except ValueError:
            print("\n That is not a number. Please try again.")

def massconvert():
    '''Choice of input mass unit.'''
    while True:
        print("\n Mass Converter \n 'p' for pounds \n 'k' for kilograms")
        cmd = input("\n Enter the letter corresponding to your mass: ")
        if cmd == 'p':
            converting_pound()
        elif cmd == 'k':
            converting_kilo()
        else:
            print('\n', "'", cmd, "'", "is not an option. \n")
            time.sleep(1)

def converting_pound():
    '''Operations to convert pounds to grams and print result.'''
    while True:
        try:
            P = float(input("\n Enter your mass: "))
            K = round(P * 0.45359237, 4)
            print("\n %s lb is %s kg" % (P, K))
            afterConvert(converting_pound, massconvert, 'pound', 'mass')
        except ValueError:
            print("\n That is not a number. Please try again.")

def converting_kilo():
    '''Operations to convert pounds to grams and print result.'''
    while True:
        try:
            K = float(input("\n Enter your mass: "))
            P = round(K / 0.45359237, 4)
            print("\n %s kg is %s lb" % (K, P))
            afterConvert(converting_kilo, massconvert, 'kilogram', 'mass')
        except ValueError:
            print("\n That is not a number. Please try again.")

def tempconvert():
    '''Choice of input temperature unit.'''
    print("\n Temperature Converter \n 'c' for Celsius \n 'f' for Fahrenheit \n 'k' for Kelvin")
    cmd = input("\n Enter the letter corresponding to your temperature: ")
    if cmd == 'c':
        converting_cel()
    elif cmd == 'f':
        converting_fah()
    elif cmd == 'k':
        converting_kel()
    else:
        print('\n', "'", cmd, "'", "is not an option. \n")
        time.sleep(1)
        tempconvert()

def converting_cel():
    '''Operations to convert celsius to fahrenheit and kelvin and print result.'''
    while True:
        try:
            C = float(input("\n Enter your temperature: "))
            F = round((C * 1.8) + 32, 3)
            K = round(C + 273.15, 3)
            print("\n %s C is %s F and %s K" % (C, F, K))
            if C < -273.15:
                zero_note()
            afterConvert(converting_cel, tempconvert, 'celsius', 'temperature')
        except ValueError:
            print("\n That is not a number. Please try again.")

def converting_fah():
    '''Operations to convert fahrenheit to celsius and kelvin and print result.'''
    while True:
        try:
            F = float(input("\n Enter your temperature: "))
            C = round((F - 32) / 1.8, 3)
            K = round(C + 273.15, 3)
            print("\n %s F is %s C and %s K" % (F, C, K))
            if F < -459.67:
                zero_note()
            afterConvert(converting_fah, tempconvert, 'fahrenheit', 'temperature')
        except ValueError:
            print("\n That is not a number. Please try again.")

def converting_kel():
    '''Operations to convert kelvin to fahrenheit and celsius and print result.'''
    while True:
        try:
            K = float(input("\n Enter your temperature: "))
            C = round(K - 273.15, 3)
            F = round((C * 1.8) + 32, 3)
            print("\n %s K is %s C and %s F" % (K, C, F))
            if F < -459.67:
                zero_note()
            afterConvert(converting_kel, tempconvert, 'kelvin', 'temperature')
        except ValueError:
            print("\n That is not a number. Please try again.")

def zero_note():
    '''Print note when input temperature is below absolute zero.'''
    time.sleep(1)
    print("\n Note however that -273.15 C, -459.67 F or 0 K is the absolute zero where atoms stop moving. It cannot get colder than that.")

def welcome():
    '''Welcome message on start.'''
    print("\n Welcome to our ORDINARY UNIT CONVERTER.")

welcome()
main_menu()




