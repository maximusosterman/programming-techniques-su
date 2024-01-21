
# Convertion functions
def celsius_to_fahrenheit(t_celsius):
    result = ((9/5) * t_celsius + 32) 
    print(f"That corrensponds to {result} Fahrenheit")
    return result

def fahrenheit_to_celsius(t_fahrenheit):
    result = (5/9) * (t_fahrenheit - 32)
    print(f"That corrensponds to {result} Celsius")
    return result

def celsius_to_kelvin(t_celsius):
    result = t_celsius + 273.15
    print(f"That corrensponds to {result} Kelvin")
    return result

def kelvin_to_celsius(t_kelvin):
    result = t_kelvin - 273.15
    print(f"That corrensponds to {result} Celsius")
    return result

def fahrenheit_to_kelvin(t_fahrenheit):
    result = (((t_fahrenheit - 32)*5)/9)+273.15
    print(f"That corrensponds to {result} Kelvin")
    return result

def kelvin_to_fahrenheit(t_kelvin):
    result = (((t_kelvin - 273.15) * 9) / 5) + 32            
    print(f"That corrensponds to {result} Fahrenheit")
    return result

def check_float(f):
    if f.replace(".", "").isnumeric() and not f.count(".") > 1:
        return float(f)
    
    while True:
        new_input = input("Give a valid float: ")
        if new_input.replace(".", "").isnumeric() and not new_input.count(".") > 1:
            return float(new_input)

def user_input():
    while True:
        choice = input("Which converstion do you want to do? ")
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= 6:
                break
        print("Please enter a valid choice!")

    if choice == 1:
        user_temprature = input("Give a temperature in Celsius: ")
        value = check_float(user_temprature)
        celsius_to_fahrenheit(value)

    if choice == 2:
        user_temprature = input("Give a temperature in Fahrenheit: ")
        value = check_float(user_temprature)
        fahrenheit_to_celsius(value)

    if choice == 3:
        user_temprature = input("Give a temperature in Celsius: ")
        value = check_float(user_temprature)
        celsius_to_kelvin(value)
    
    if choice == 4:
        user_temprature = input("Give a temperature in Kelvin: ")
        value = check_float(user_temprature)
        kelvin_to_celsius(value)

    if choice == 5:
        user_temprature = input("Give a temperature in Fahrenheit: ")
        value = check_float(user_temprature)
        fahrenheit_to_kelvin(value)

    if choice == 6:
        user_temprature = input("Give a temperature in Kelvin: ")
        value = check_float(user_temprature)
        kelvin_to_fahrenheit(value)


if __name__ == '__main__':
    print("Temperature converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit\n\n")
    user_input()
    