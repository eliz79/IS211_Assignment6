#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function for temperature conversions."""

#Author - Erica Liz

def convertCelsiusToKelvin(temp):
    """A conversion from Celsius to Kelvin
    Args:
        total(int): formula to calculate conversion
    Return: a float value of conversion
    Example:
        >>> convertCelsiusToKelvin(300)
        573.15
    """
    total = temp + 273.15
    return float("%.3f" % total)
    

def convertCelsiusToFahrenheit(temp):
    """A conversion from Celsius to Fahrenheit.
    Args:
        total(int): formula to calculate conversion
    Return: a float value of conversion
    Example:
        >>> convertCelsiusToFarenheit(300)
        572.0
    """
    total = (1.8 * temp) + 32
    return float("%.3f" % total)


def convertFahrenheitToKelvin(temp):
    """A conversion from Fahrenheit to Kelvin.
    Args:
        total(int): formula to calculate conversion
    Return: a float value of conversion
    Example:
        >>> convertFahrenheitToKelvin(300)
        422.039
    """
    total = ((temp - 32) / 1.8) + 273.15
    return float("%.3f" % total)


def convertFahrenheitToCelsius(temp):
    """A conversion from Farenheit to Celsius.
    Args:
        total(int): formula to calculate conversion
    Return: a float value of conversion
    Example:
        >>> convertFahrenheitToCelsius(300)
    148.889
    """
    total = (temp - 32) / 1.8
    return float("%.3f" % total)


def convertKelvinToCelsius(temp):
    """A conversion from Kelvin to Celsius.
    Args:
        total(int): formula to calculate conversion
    Return: a float value of conversion
    Example:
        >>> convertKelvinToCelsius(300)
    26.85
    """
    total = temp - 273.15
    return float("%.3f" % total)
    

def convertKelvinToFahrenheit(temp):
    """A conversion from Kelvin to Fahrenheit.
    Args:
        total(int): formula to calculate conversion
    Return: a float value of conversion
    Example:
        >>> convertKelvinToFahrenheit(300)
    80.33
    """
    total = (temp - 273.15) * 1.8 + 32
    return float("%.3f" % total)
