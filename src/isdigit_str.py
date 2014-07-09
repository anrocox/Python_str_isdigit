#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

How to know if the characters of a string are digits in python?

¿Como saber si los caracteres de un string son digitos en python?
'''

#create a str
s = '1¹2₂'
print(s)

#verify if all characters in the string are digits. Return True or False.
#Include all characters that have the Unicode numeric property with the value
#Numeric_Type=Digit or Numeric_Type=Decimal.
print(s.isdigit())

#create a str
s = '¹5¾'
print(s)

#return False because the ¾ character is of type numeric.
print(s.isdigit())
