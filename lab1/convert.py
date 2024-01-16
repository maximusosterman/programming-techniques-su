
# Convertion functions
def celsius_to_fahrenheit(t_celsius):
    result = ((9/5) * t_celsius + 32) 
    print(f"That corrensponds to {result} Fahrenheit")

def fahrenheit_to_celsius(t_fahrenheit):
    result = (5/9) * (t_fahrenheit - 32)
    print(f"That corrensponds to {result} Celsius")

def celsius_to_kelvin(t_celsius):
    result = t_celsius + 273.15
    print(f"That corrensponds to {result} Kelvin")

def kelvin_to_celsius(t_kelvin):
    result = t_kelvin - 273.15
    print(f"That corrensponds to {result} Celsius")

def fahrenheit_to_kelvin(t_fahrenheit):
    result = (((t_fahrenheit - 32)*5)/9)+273.15
    print(f"That corrensponds to {result} Kelvin")

def kelvin_to_fahrenheit(t_kelvin):
    result = (((t_kelvin - 273.15) * 9) / 5) + 32            
    print(f"That corrensponds to {result} Fahrenheit")


def user_input():
    choice = float(input("Wich converstion do you want to do? "))

    if choice == 1:
        user_temprature = float(input("Give a temperature in Celsius: "))
        celsius_to_fahrenheit(user_temprature)

    if choice == 2:
        user_temprature = float(input("Give a temperature in Fahrenheit: "))
        fahrenheit_to_celsius(user_temprature)

    if choice == 3:
        user_temprature = float(input("Give a temperature in Celsius: "))
        celsius_to_kelvin(user_temprature)
    
    if choice == 4:
        user_temprature = float(input("Give a temperature in Kelvin: "))
        kelvin_to_celsius(user_temprature)

    if choice == 5:
        user_temprature = float(input("Give a temperature in Fahrenheit: "))
        fahrenheit_to_kelvin(user_temprature)

    if choice == 6:
        user_temprature = float(input("Give a temperature in Kelvin: "))
        kelvin_to_fahrenheit(user_temprature)


if __name__ == '__main__':
    print("Temperature converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit\n\n")
    user_input()
    