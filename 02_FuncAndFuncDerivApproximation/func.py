import numpy

def evaluate_f(x):
    return numpy.exp(x)/( numpy.cos(x)**3 + numpy.sin(x)**3 )

def evaluate_derivative_f(x):
    return (numpy.exp(x)*(numpy.cos(3.0*x) + numpy.sin(3.0*x)/2.0 + (3.0*numpy.sin(x))/2.0))/(numpy.cos(x)**3 + numpy.sin(x)**3)**2

