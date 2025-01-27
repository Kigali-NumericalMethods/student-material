
#
# Evaluate the recurrence relation
# given by the logistic map
#   x_n = r x_{n-1}(1 - x_{n-1})
#

n = 3


r = 2.0
x0 = 2.0    # set initial condition

t1 = x0    # set temp variable t1 to initial condition

if n == 0:
  xn = t1
else:
  for i in range(1,n+1):    # note the n+1 because we want to include n in our loop
    xn = r * t1 * (1.0 - t1)
    t1 = xn
  xn = t1

print('xn(',n,') =',xn)

# expected answer
# x0 = 2
# x1 = 2 * 2 * (1-2) = -4
# x2 = 2 * (-4) * (1 + 4) = -40
# x3 = 2 * (-40) * (1 + 40) = -3280
