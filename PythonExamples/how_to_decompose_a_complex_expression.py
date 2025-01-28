#
# Suppose we wanted to compute
#  f =  sqrt( | sin(cos(exp(x)) + pi) + 3 | )
#
# This expression is a bit too much to write out on one line
# It is desirable to decompose the function into a series of intermediate calculations.
# We do this using temporary variables

# As a first step it is helpful to write the expression like this
#  f =  sqrt(
#                |
#                    sin(
#                        cos(
#                            exp(x)
#                            ) + pi
#                        ) + 3
#                |
#            )

import math

# Given some input
x = 0.11


t1 = math.exp(x) # Compute temperary variable for the deepest part of the calculation
t2 = math.cos( t1 ) + math.pi # Use previous temp variable (t1) to compute another temp variable depth + 1 term
t3 = math.sin( t2 ) + 3.0
t4 = math.fabs( t3 )
t5 = math.sqrt( t4 )

f = t5
print(f)
