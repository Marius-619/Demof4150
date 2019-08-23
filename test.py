#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:41:48 2019

@author: Marius
"""

from math import *

h = 0.0001

def Derivative_2pt(function,x):
    return (function(x+h)-function(x))/h

def Derivative_3pt(function,x):
    return (function(x+h)-function(x-h))/(2*h)

def error(func,exact):
    epsilon = log10(abs((func-exact)/exact))
    return epsilon

print error(Derivative_2pt(atan,sqrt(2)),1./3)
