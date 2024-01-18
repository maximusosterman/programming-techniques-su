from convert import *
import pytest

def test_celsius_to_fahrenheit():
    result = celsius_to_fahrenheit(0)
    assert result == 32

def test_fahrenheit_to_celsius():
    result = fahrenheit_to_celsius(32)
    assert result == 0

def test_celsius_to_kelvin():
    result = celsius_to_kelvin(0)
    assert result == 273.15
    
def test_kelvin_to_celsius():
    result = kelvin_to_celsius(273.15)
    assert result == 0

