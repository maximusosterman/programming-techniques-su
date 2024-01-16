
# Convertion functions
def celsius_to_fahrenheit(t_celsius):
    return ((9/5) * t_celsius + 32) 

def fahrenheit_to_celsius(t_fahrenheit):
    return (5/9) * (t_fahrenheit - 32)

def celsius_to_kelvin(t_celsius):
    return t_celsius + 273.15

def kelvin_to_celsius(t_kelvin):
    return t_kelvin - 273.15

def fahrenheit_to_kelvin(t_fahrenheit):
    return (((t_fahrenheit - 32)*5)/9)+273.15

def kelvin_to_fahrenheit(t_kelvin):
    return (((t_kelvin - 273.15) * 9) / 5) + 32            

if __name__ == '__main__':
    print("Temperature converter")
    