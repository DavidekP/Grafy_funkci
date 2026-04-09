import numpy as np

def linear(x, a=1.0, b=0.0):
    """f(x) = a*x + b"""
    return a * x + b

def quadratic(x, a=1.0, b=0.0, c=0.0):
    """f(x) = a*x^2 + b*x + c"""
    return a * x**2 + b * x + c

def sine(x, k=1.0, amplitude=1.0, phase=0.0):
    """f(x) = amplitude * sin(k*x + phase)"""
    return amplitude * np.sin(k * x + phase)

def exponential(x, a=1.0):
    """f(x) = e^(a*x)"""
    return np.exp(a * x)

def reciprocal(x, a=1.0):
    """f(x) = a/x ; pozor na x=0 (řešíme malým posunem)"""
    eps = 1e-9
    return a / (x + eps)